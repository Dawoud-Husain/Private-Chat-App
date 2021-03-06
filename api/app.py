"""
*************************************************************************************************************
Author: Dawoud Husain
Date: September 3, 2021



*************************************************************************************************************
"""

"""
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
Imports
"""
from flask import Flask, app, request, jsonify, render_template, redirect
import os
import pusher

from database import db_session
from models import User, Channel, Message

from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

"""
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
App Config
"""


app = Flask(__name__)
# app = Flask(__name__, static_folder='C:\Users\dawou\Documents\PersonalCondingProjects\Swift--Chat-2\dist', static_url_path='/')

# Initilize Python Pusher libary
pusher = pusher.Pusher(
    app_id= "1214203",
    key= "c0910161aefffaec26d8",
    secret= "acf2703d25caa6000f9e",
    cluster= "us2", ssl=True)

# pusher = pusher.Pusher(
#     app_id=os.getenv('PUSHER_APP_ID'),
#     key=os.getenv('PUSHER_KEY'),
#     secret=os.getenv('PUSHER_SECRET'),
#     cluster=os.getenv('PUSHER_CLUSTER'),
#     ssl=True)

# Configure flask_jwt_extended package to use Flask app config
app.config['JWT_SECRET_KEY'] = 'something-super-secret'
jwt = JWTManager(app)


"""
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
Default Endpoints/Routes
"""
# Default route (used to see if flask is working)
@app.route('/')
def index():
    return jsonify("Pong!")

# Close the connetction to the database once an operation is complete 
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

"""
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
Login Endpoints/Routes
"""

# Register POST route that will accept JSON objects containing new user details (username and password)
@app.route('/api/register', methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = generate_password_hash(data.get("password"))

    # attempt to add the user to the database, and return a sucess/failure message

    try:    
        new_user = User(username=username, password=password)
        db_session.add(new_user)
        db_session.commit()
    except:
        return jsonify({
            "status": "error",
            "message": "Could not add user"
        })

    return jsonify({
        "status": "success",
        "message": "User added successfully"
    }), 201


# Login route accepts JSON objects containing user information and validates it
@app.route('/api/login', methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({
            "status": "failed",
            "message": "Failed getting user"
        }), 401

    # Generate a token
    access_token = create_access_token(identity=username)

    return jsonify({
        "status": "success",
        "message": "login successful",
        "data": {
            "id": user.id,
            "token": access_token,
            "username": user.username
        }
    }), 200

"""
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
Chat Endpoints/Routes
"""

# Endpoint to generate a channel name for both users to communicate
@app.route('/api/request_chat', methods=["POST"])
# protect the route by checking the JWT token
@jwt_required
def request_chat():
    # Get user ID of users
    request_data = request.get_json()
    from_user = request_data.get('from_user', '')
    to_user = request_data.get('to_user', '')
    to_user_channel = "private-notification_user_%s" % (to_user)
    from_user_channel = "private-notification_user_%s" % (from_user)

    # check if there is a channel that already exists between this two user
    channel = Channel.query.filter(Channel.from_user.in_([from_user, to_user])) \
                           .filter(Channel.to_user.in_([from_user, to_user])) \
                           .first()
    
    # If channel does not exist, then generate a channel
    if not channel:
        chat_channel = "private-chat_%s_%s" % (from_user, to_user)
        new_channel = Channel()
        new_channel.from_user = from_user
        new_channel.to_user = to_user
        new_channel.name = chat_channel
        db_session.add(new_channel)
        db_session.commit()

    # Else Use the channel name stored on the database
    else:
        chat_channel = channel.name

    data = {
        "from_user": from_user,
        "to_user": to_user,
        "from_user_notification_channel": from_user_channel,
        "to_user_notification_channel": to_user_channel,
        "channel_name": chat_channel,
    }

    # Trigger an event to the other user
    pusher.trigger(to_user_channel, 'new_chat', data)

    return jsonify(data)

# Authenticate Pusher Channel Subscription
@app.route("/api/pusher/auth", methods=['POST'])
@jwt_required
def pusher_authentication():
    channel_name = request.form.get('channel_name')
    socket_id = request.form.get('socket_id')

    auth = pusher.authenticate(
        channel=channel_name,
        socket_id=socket_id
    )

    return jsonify(auth)

# Send message accross users
@app.route("/api/send_message", methods=["POST"])
@jwt_required
def send_message():
    request_data = request.get_json()
    from_user = request_data.get('from_user', '')
    to_user = request_data.get('to_user', '')
    message = request_data.get('message', '')
    channel = request_data.get('channel')

    new_message = Message(message=message, channel_id=channel)
    new_message.from_user = from_user
    new_message.to_user = to_user
    db_session.add(new_message)
    db_session.commit()

    message = {
        "from_user": from_user,
        "to_user": to_user,
        "message": message,
        "channel": channel,
        # "sentiment": getSentiment(message)
    }

    # Trigger an event to the other user
    pusher.trigger(channel, 'new_message', message)

    return jsonify(message)

# Get all users from database
@app.route('/api/users')
@jwt_required
def users():
    users = User.query.all()
    return jsonify(
        [{"id": user.id, "userName": user.username} for user in users]
    ), 200

# Get all messages in a particular channel
@app.route('/api/get_message/<channel_id>')
@jwt_required
def user_messages(channel_id):
    messages = Message.query.filter(Message.channel_id == channel_id).all()

    return jsonify([
        {
            "id": message.id,
            "message": message.message,
            "to_user": message.to_user,
            "channel_id": message.channel_id,
            "from_user": message.from_user,
            # "sentiment": getSentiment(message.message)
        }
        for message in messages
    ])

"""
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
Flask configuration
"""

# Running Flask Applicatoin
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)