# -*- coding: utf-8 -*-

import zipfile
import settings
import os

def un_zip(file_name):
    """unzip zip file"""

    file_path = settings.ROOT_DIR + "/source/"+ file_name

    zip_file = zipfile.ZipFile(file_path + ".zip")

    extract_path = file_path + "_files"
    if os.path.isdir(extract_path):
        pass
    else:
        os.mkdir(extract_path)

    for names in zip_file.namelist():
        zip_file.extract(names, extract_path)
        
    zip_file.close()

    return extract_path
