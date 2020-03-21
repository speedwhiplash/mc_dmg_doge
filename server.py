from flask import Flask, url_for
app = Flask(__name__)

url_for('/static', filename='./static')

@app.route('/')
def index():
    return 'static/index.html'
