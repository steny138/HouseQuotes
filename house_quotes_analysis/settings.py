# -*- coding: utf-8 -*-

import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

InfrastructureBase = declarative_base()
Base = declarative_base()

InfrastructureEngine = create_engine('sqlite:///..//source//infrastructure.sqlite', echo=False)
Engine = create_engine('sqlite:///..//source//db.sqlite', echo=False)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
ROOT_DIR = os.path.abspath(os.path.join(ROOT_DIR, os.pardir))

