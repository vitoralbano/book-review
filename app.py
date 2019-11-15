from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello world"
