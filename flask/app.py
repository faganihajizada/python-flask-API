from flask import Flask
from flask_cors import CORS, cross_origin

#Create a flask instance

app = Flask(__name__)
CORS(app)