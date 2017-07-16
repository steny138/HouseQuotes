# -*- coding: utf-8 -*-

import os
import sys
import csv
import xml.etree.cElementTree as etree

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import RealPriceCase
from settings import Base, Engine, ROOT_DIR
import zipper

# 1. 創建Tables
Base.metadata.create_all(Engine)
Session= sessionmaker(bind=Engine)
session = Session()


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'iso-8859-1') for cell in row]

def match_csv(f):
    if len(os.path.splitext(f)[0].split('_')) == 4:
        return os.path.splitext(f)[-1].lower() == ".csv"
    else:
        return False

def csv_rows(extract_csv_file_path):
    result = []

    with open(os.path.join(extract_path, extract_csv_file_path), 'r') as f:
        # reader = unicode_csv_reader(f)
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 28:
                real_price_case = [x.decode('big5').encode('utf-8') for x in row]
                case = RealPriceCase(real_price_case)
                result.append(case)

    return result

def match_xml(f):
    if len(os.path.splitext(f)[0].split('_')) == 4:
        return os.path.splitext(f)[-1].lower() == ".xml"
    else:
        return False

def xml_row(extract_csv_file_path):
    result = []
    print extract_csv_file_path
    try:
        tree=etree.parse(os.path.join(extract_path, extract_csv_file_path))
        root=tree.getroot()
    
        for child in root.findall(u'買賣'):
            row = []
            # find all xml tags
            for one in child.getchildren():
                # print one.tag,':',one.text
                row.append(one.text)

            if len(row) == 28:
                real_price_case = [x for x in row]
                case = RealPriceCase(real_price_case)
                result.append(case)
    except Exception as e:
        print e
    return result

    # for child in root:
    #     print child.tag  # 第一层节点

    #     for grandchild in child:
    #     print grandchild.tag  # 第二层节点
 
if __name__ == '__main__':
    files = ["2017S2"]
    for fileName in files:
        # 先解壓縮
        extract_path = zipper.un_zip(fileName)
        #取得檔案清單
        extract_csv_files = [f for f in os.listdir(extract_path) if match_xml(f)]

        for extract_csv_file_path in extract_csv_files:
            cases = xml_row(extract_csv_file_path)
            for case in cases:
                session.add(case)

        session.commit()

    session.close()
