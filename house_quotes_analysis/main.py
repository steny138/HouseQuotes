# -*- coding: utf-8 -*-

import sys
import io
import os
import csv
import xml.etree.cElementTree as etree
from datetime import date

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print(sys.version)
print(sys.getdefaultencoding())
print(sys.stdout.encoding)

from sqlalchemy import create_engine, func
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from models.RealPriceCase import RealPriceCase
from models.infrastructure import District, DealPurpose
from settings import Base, InfrastructureBase, InfrastructureEngine, Engine, ROOT_DIR
from parse import ParseAddress

# 2. 建立連線
Session = sessionmaker(bind=InfrastructureEngine)
infrastructure_session = Session()

InfrastructureBase.metadata.create_all(InfrastructureEngine)

OriSession = sessionmaker(bind=Engine)
ori_session = OriSession()

if __name__ == '__main__':
    # 獲得數據筆數
    count = ori_session.query(RealPriceCase).count()
    print("總共有%d筆" % count)
    # 查詢速度更快的方法
    count = ori_session.query(func.count(
        '1')).select_from(RealPriceCase).scalar()
    print("總共有%d筆" % count)

    limit = 1000
    index = 0
    while index * limit <= count:
        for instance in ori_session.query(RealPriceCase).offset(index * limit).limit(limit).all():
            address = ParseAddress.parse(instance.address)
            print(instance.id, instance.address)
            if not all(e in address for e in ('city', 'district')):
                continue

            # district
            ret = infrastructure_session.query(District).filter(District.city == address['city'])\
                .filter(District.district == address['district'])\
                .count()

            if ret == 0 and len(address['city']) <= 5:
                case = District(address['city'], address['district'])
                infrastructure_session.add(case)
                
            # purpose
            ret = infrastructure_session.query(DealPurpose)\
                    .filter(DealPurpose.purpose == instance.dealType)\
                    .count()

            if ret == 0:
                purpose = DealPurpose(instance.dealType)
                infrastructure_session.add(purpose)

            infrastructure_session.commit()

        index += 1
    print("end")
