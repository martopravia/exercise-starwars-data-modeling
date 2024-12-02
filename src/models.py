import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(120), unique=True, nullabase=False)
    firstname = Column(String(120), nullabase=False)
    lastname = Column(String(120), nullabase=False)
    email = Column(String(150), unique=True, nullabase=False)


class Comment(Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment_text = Column(String)
    author_id = Column(Integer, Foreing_key("User.id"))
    post_id = Column(Integer, Foreign_key("Post.id"))
    user = relationship("User", backref="comment")

class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, Foreing_key("User.id"),nullabase=False)
    user = relationship("User", backref="post")
    
class Media(Base):
    __tablename__ = "Media"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum, nullabase=False)
    url = Column(String, nullabase=False)
    post_id = Column(Integer, Foreing_key("Post.id"),nullabese=False)
    post = relationship("Post", backref="media")
    
class Follower(Base):
    __tablename__ = "Follower"
    user_from_id = Column(Integer, primary_key=True, nullabase=False)
    user_to_id = Column(Integer, primary_key=True, Foreing_key("User.id"), nullabase=False)
    user_from = relationship("User", backref="follower")
    
    
    
    
    
    
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
