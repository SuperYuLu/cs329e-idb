from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import home, artists, albums, songs, about, datapagesAutoGen
from sqlalchemy import create_engine
