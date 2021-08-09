import requests
from flask import Flask,Flask, request, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=97071d9cfaf6a74c61ab998ed28f6259'
    city = "Boston"
    req = requests.get(url.format(city)).json()
    print (req)

    weather_data = {
        'city' : city, 
        'tempreture' : req['main']['temp'],
        'description' : req['weather'][0]['description'],
        'icon' : req['weather'][0]['icon']
    }

    return render_template('index.html', weather=weather_data)
