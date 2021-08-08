import requests
from flask import Flask,Flask, request, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=97071d9cfaf6a74c61ab998ed28f6259'
    return render_template('index.html')
