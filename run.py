import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

if __name__ == "__main__":
    app.run(host=os.getenv("IP"),port=os.getenv("PORT"), debug=True)

@app.route("/<username>")
def user (username):
    return "Hi "+username

@app.route("/<username>/<message>")
def send_message (username,message):
    return "{0}: {1}".format(username,message)