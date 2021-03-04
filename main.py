from flask import Flask
import os
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/landing_page', methods=["GET", "POST"])
def home_page():

    return render_template("Home_Page.html")