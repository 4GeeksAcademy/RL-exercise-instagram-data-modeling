import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

class Comment(Base):
    __tablename__ = 'comment'
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    text_comment = Column(String(250))
    likes = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    
class Post(Base): 
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    interactions = Column(Integer)
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    post_id = Column (Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship (User)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
