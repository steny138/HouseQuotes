# -*- coding: utf-8 -*-

import hashlib

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from settings import InfrastructureBase

class District(InfrastructureBase):
    __tablename__ = 'Districts'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    district = Column(String)

    def __init__(self, c, d):
        self.city = c
        self.district = d

    def __repr__(self):
        return "'{}'-'{}'".format(
            self.city,
            self.district
        )

class DealPurpose(InfrastructureBase):
    __tablename__ = 'DealPurposes'

    id = Column(Integer, primary_key=True)
    purpose = Column(String)

    def __init__(self, p):
        self.purpose = p

    def __repr__(self):
        return self.purpose
        