from flask.helpers import flash, url_for
import requests
from flask import Flask,Flask, request, render_template,jsonify,redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'testkey'
database = SQLAlchemy(app)

class City(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.Integer, nullable=False)


@app.route('/')
def index():
    city_list = City.query.all()
    weather_city_list = []

    for city in city_list:
        req = getCityData(city.name)
        weather_data = {
            'city' : city, 
            'tempreture' : req['main']['temp'],
            'description' : req['weather'][0]['description'],
            'icon' : req['weather'][0]['icon']
        }
        weather_city_list.append(weather_data)

    return render_template('index.html', weathers=weather_city_list)

def getCityData(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&appid=97071d9cfaf6a74c61ab998ed28f6259'
    req = requests.get(url).json()
    return req



@app.route('/', methods=['POST'])
def index_post():
    flash_message = ''
    new_city = request.form.get('city')
    
    if new_city:
        check_city  = City.query.filter_by(name=new_city).first()
        if not check_city:
            valid_city_check = getCityData(new_city)
            if valid_city_check['cod'] == 200:
                nc_object = City(name=new_city)
                database.session.add(nc_object)
                database.session.commit()
            else:
                flash_message = 'While we appriciate your input, but we are unable to service this city. Either the city does not exist or we do not have weather stations nearby'
        else:
            flash_message = 'City already on dashboard'
    if flash_message:
        flash(flash_message,'alert')
    else:
        flash('Congratulations')

    return redirect(url_for('index'))
    
@app.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    database.session.delete(city)
    database.session.commit()

    flash(f'Removed { city.name }', 'success')
    return redirect(url_for('index'))




