# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from settings import Base

class RealPriceCase(Base):
    __tablename__ = 'RealPriceCases'
