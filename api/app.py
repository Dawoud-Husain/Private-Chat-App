from flask import Flask, app, request, jsonify, render_template, redirect
import os
import pusher

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify("pong!")

#running the flask application
if __name__ == "__main__":
    app.run()

    