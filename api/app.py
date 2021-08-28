from flask import Flask, app, request, jsonify, render_template, redirect
import os
import pusher

# ./api/app.py

# [...]
from database import db_session
from models import User, Channel, Message
# [...] 

  #[...]
from werkzeug.security import generate_password_hash, check_password_hash
#[...]

from flask_jwt_extended import JWTManager, jwt_required, create_access_toxken,get_jwt_identity

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify("pong!")

#running the flask application
if __name__ == "__main__":
    app.run()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# Api Regester  route, accepts JSON object containing new user detials 
@app.route('/api/register', methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = generate_password_hash(data.get("password"))
    
    try:
        new_user = User(username=username, password=password)
        db_session.add(new_user)
        db_session.commit()
    # Error Message
    except:
        return jsonify({
            "status": "error",
            "message": "Could not add user"
        })
    
    # Sucess Message
    return jsonify({
        "status": "success",
        "message": "User added successfully"
    }), 201