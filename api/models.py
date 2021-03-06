from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

# User model storing the username and password
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(128))
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % (self.username)

# Channel model for storing the id, name, from_user, and to_user for each channel
class Channel(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    from_user = Column(Integer, ForeignKey('users.id'))
    to_user = Column(Integer, ForeignKey('users.id'))

# message model storing the id, text, from_user, to_user and channel_id
class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    message = Column(Text)
    from_user = Column(Integer, ForeignKey('users.id'))
    to_user = Column(Integer, ForeignKey('users.id'))
    channel_id = Column(Integer, ForeignKey('channels.id'))