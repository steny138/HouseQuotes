# -*- coding: utf-8 -*-

import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

Engine = create_engine('sqlite:///source//db.sqlite', echo=False)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
