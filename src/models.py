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
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment_text = Column(String)
    author_id = Column(Integer)
    post_id = Column(Integer)


    
    
    
    
    
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
