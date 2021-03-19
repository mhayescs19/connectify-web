from flask import Flask
import os
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/landing_page', methods=["GET", "POST"])
def landing_page():
    return render_template("landing_page.html")


@app.route('/timeline/post')
def individual_post():
    return render_template("individualPost.html")

if __name__ == "__main__":
    app.run(port='80', host='127.0.0.1')