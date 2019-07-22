import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "reandomstring"
messages = []

def add_messages(username, message):
    """add messages to messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(messages_dict)

@app.route('/', methods = ["GET", "POST"])
def index():
    """main page with instructions"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html", page_title="Home")

@app.route('/<username>', methods= ["GET", "POST"])
def user(username):
    """display messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_messages(username, message)
        return redirect(session["username"])
        
    return render_template("chat.html", username=username, chat_messages=messages, page_title="Chat")

@app.route('/<username>/<message>')
def send_message(username, message):
    """create a message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)