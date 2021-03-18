from flask import Flask
import os
from flask import render_template

app = Flask(__name__)

@app.route('/landing_page', methods=["GET", "POST"])
def landing_page():
    return render_template("Landing_Page.html")

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/timeline/post')
def individual_post():

    return render_template("individualPost.html")