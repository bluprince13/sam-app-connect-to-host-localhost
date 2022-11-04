# https://flask.palletsprojects.com/en/2.2.x/quickstart/
# Run using `flask --app hello run`

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"