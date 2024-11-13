from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Lancie!'

@app.route('/gats')
def home():
    return 'Hello, Gatsie!'

@app.route('/about')
def about():
    return 'About'
