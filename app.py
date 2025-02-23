from flask import Flask, render_template
from dotenv import load_dotenv

import os

load_dotenv(verbose=True)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')
