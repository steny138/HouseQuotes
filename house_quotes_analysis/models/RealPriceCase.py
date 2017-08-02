# -*- coding: utf-8 -*-

import hashlib

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from settings import Base

class RealPriceCase(Base):
    __tablename__ = 'RealPriceCases'

    id = Column(Integer, primary_key=True)
    area = Column(String)
    address = Column(String)
    dealType = Column(String)
    landMeasure = Column(String)
    useType = Column(String)
    dealDate = Column(String)
    dealCount = Column(String)
    totalFloor = Column(String)
    caseType = Column(String)
    purpose = Column(String)
    material = Column(String)
    finishDate = Column(String)
    buildingMeasure = Column(String)
    livinroomCount = Column(String)
    bedroomCount = Column(String)
    bathroomCount = Column(String)
    hasSeparate = Column(String)
    hasManage = Column(String)
    amount = Column(String)
    unitPrice = Column(String)
    carType = Column(String)
    carMeasure = Column(String)
    carAreaAmount = Column(String)
    remark = Column(String)
    numberkey = Column(String)

    def __init__(self, lst):
        self.area = lst[0]
        self.dealType = lst[1]
        self.address = lst[2]
        self.landMeasure = lst[3]
        self.useType = lst[4]
        self.dealDate = lst[7]
        self.dealCount = lst[8]
        self.totalFloor = lst[10]
        self.caseType = lst[11]
        self.purpose = lst[12]
        self.material = lst[13]
        self.finishDate = lst[14]
        self.buildingMeasure = lst[15]
        self.livinroomCount = lst[17]
        self.bedroomCount = lst[16]
        self.bathroomCount = lst[18]
        self.hasSeparate = lst[19]
        self.hasManage = lst[20]
        self.amount = lst[21]
        self.unitPrice = lst[22]
        self.carType = lst[23]
        self.carMeasure = lst[24]
        self.carAreaAmount = lst[25]
        self.remark = lst[26]
        self.numberkey = lst[27]

    def whatisthis(self, s):
        if isinstance(s, str):
            print "ordinary string"
        elif isinstance(s, unicode):
            print "unicode string"
        else:
            print "not a string"

    def __repr__(self):
        return "'{}','{}','{}'".format(
            self.dealDate,
            self.address,
            self.amount
        )