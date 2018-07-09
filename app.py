import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to the Source to image openshift test!"

@app.route('/how are you')
def hello():
    return 'This is the application for source to image?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
