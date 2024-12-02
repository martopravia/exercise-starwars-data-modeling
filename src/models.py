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
    author_id = Column(Integer)
    post_id = Column(Integer)

class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullabase=False)
    
class Media(Base):
    __tablename__ = "Media"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum, nullabase=False)
    url = Column(String, nullabase=False)
    
class Follower(Base):
    __tablename__ = "Follower"
    user_from_id = Column(Integer, primary_key=True, nullabase=False)
    user_to_id = Column(Integer, primary_key=True, nullabase=False)

    
    
    
    
    
    
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
