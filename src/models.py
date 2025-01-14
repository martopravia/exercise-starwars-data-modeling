import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    subscription_date = Column(DateTime, default=datetime.utcnow)
    favorites = relationship("Favorite", backref="user")

class Planet(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(120), nullable=False)
    description = Column(String(255))
    climate = Column(String(100))
    terrain = Column(String(100))
    favorites = relationship("Favorite", backref="planet")

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(120), nullable=False)
    species = Column(String(100))
    gender = Column(String(50))
    birth_year = Column(String(50))
    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=True)  
    planet = relationship("Planet", backref="characters") 
    favorites = relationship("Favorite", backref="character")

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    content = Column(String(255), nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorites.id"), nullable=False)
    user = relationship("User", backref="comments")
    favorite = relationship("Favorite", backref="comments")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
