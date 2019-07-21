import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """add messages to messages list"""
    messages.append("{}: {}".format(username, message))

def get_all_messages():
    """Get all messages and seperate them with a `br`"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """main page with instructions"""
    return "To send message use /USERNAME/MESSAGE"

@app.route('/<username>')
def user(username):
    """display messages"""
    return "<h1>Welcome, {0}</h1> {1} ".format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message(username, message):
    """create a message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)