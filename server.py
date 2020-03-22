from flask import Flask
from flask import render_template
app = Flask(__name__)

# url_for('/static', filename='./static')

@app.route('/')
def index():
    return render_template("./static/index.html")
