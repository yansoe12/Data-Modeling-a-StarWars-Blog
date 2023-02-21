import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class User(Base):
    __tablename__ = 'User'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planetas'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)

class Characters(Base):
    __tablename__ = 'Characters'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    manufacturer = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    max_atmospheric_speed = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(50), nullable=False)
    MGLT = Column(Integer, nullable=False)
    starship_class = Column(String(250), nullable=False)
    pilot = relationship("character", back_populates="character_id")
    film = relationship("film", back_populates="vehicle_id")
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)

class Film(Base):
    __tablename__= 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)    
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(String(250), nullable=False)    
    director = Column(String(250), nullable=False)    
    producer = Column(String(250), nullable=False)    
    release_date = Column(String(250), nullable=False)    
    character = relationship("character", back_populates="character_id")
    planet = Column(Integer, ForeignKey("planet.id"))
    starship = Column(Integer, ForeignKey("starship.id"))
    vehicles= Column(Integer, ForeignKey("vehicle.id"))
    species= Column(Integer, ForeignKey("specie.id"))
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)

class Specie(Base):
    __tablename__= 'specie'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(50), nullable=False)
    designation = Column(String(50), nullable=False)
    average_height = Column(Integer, nullable=False)
    skin_colors = relationship("color", back_populates="vehicle_id")
    hair_colors = Column(Integer, ForeignKey("color.id"))
    eye_colors = Column(Integer, ForeignKey("color.id"))
    average_lifespan = Column(Integer, nullable=False)
    homeworld = Column(Integer, ForeignKey("planet.id"))
    language = Column(Integer, ForeignKey("languaje.id"))
    people = Column(Integer, ForeignKey("character.id"))


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
