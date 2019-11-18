from flask import Flask, render_template
from dotenv import load_dotenv
from .routes.web import routes_web

import os

load_dotenv(verbose=True)

app = Flask(__name__)
app.register_blueprint(routes_web)
