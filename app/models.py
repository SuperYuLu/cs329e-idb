import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know
# that our classes are special SQLAlchemy classes that
# corresponds to tables in our DB)
Base = declarative_base()


class Artists(Base):
    __tablename__ = 'artists'

    name = Column(String(80), primary_key=True, nullable=False)
    no_members = Column(Integer)
    start_date = Column(Date)
    origin = Column(String(80))
    no_albums = Column(Integer)

class Albums(Base):
    __tablename__ = 'albums'

    name = Column(String(80), primary_key=True, nullable=False)

class Songs(Base):
    __tablename__ = 'songs'

    name = Column(String(80), primary_key=True, nullable=False)
    artist = Column(String(80))
    rank = Column(Integer)
    song_link = Column(Text)
    genre = Column(String(20))
    release_date = Column(Date)


SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:asd123@localhost/bookdb')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
