#!/usr/bin/env python3
""" 0-app.py """
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ A route that renders an html template """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
