from flask.helpers import url_for
import requests
from flask import Flask,Flask, request, render_template,jsonify,redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)

class City(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.Integer, nullable=False)


@app.route('/')
def index():
    city_list = City.query.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=97071d9cfaf6a74c61ab998ed28f6259'

    weather_city_list = []

    for city in city_list:
        req = requests.get(url.format(city.name)).json()
    
        weather_data = {
            'city' : city.name, 
            'tempreture' : req['main']['temp'],
            'description' : req['weather'][0]['description'],
            'icon' : req['weather'][0]['icon']
        }
        weather_city_list.append(weather_data)

    return render_template('index.html', weathers=weather_city_list)



@app.route('/', methods=['POST'])
def index_post():

    new_city = request.form.get('city')

    if new_city:
        nc_object = City(name=new_city)
        database.session.add(nc_object)
        database.session.commit()
    return redirect(url_for('index'))
    return render_template('index.html', weathers=weather_city_list)


