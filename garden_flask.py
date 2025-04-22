from flask import Flask

app = Flask(__name__)

@app.route('/')
def happy_earth_day():
    return '<p>Happy Earth Day!</p>'