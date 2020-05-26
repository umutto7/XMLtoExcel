import os, errno
import timeit
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter
# --------> get desktop path

def excel_writer():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
    excel_name = "ithalatconverter" + date_time

    path = os.path.join(os.path.expanduser("~"), "Desktop", "XMLParser_Sonuc", str(excel_name) + '.xlsx')
    excel_writer.writer = ExcelWriter(path)

def gelendosya():

    currentDirectory = os.getcwd()
    desktopPath = os.path.join(os.environ["HOMEPATH"], "Desktop")
    os.chdir(desktopPath)
    try:
        os.mkdir('XMLParser_Gelen')
        gelendosya.dosyadurumu = "yok"

    except FileExistsError:
        print('------->File alreeady exists')
        gelendosya.dosyadurumu = "var"
        pass
    os.chdir(currentDirectory)


def sonucdosya():

    currentDirectory = os.getcwd()
    desktopPath = os.path.join(os.environ["HOMEPATH"], "Desktop")
    os.chdir(desktopPath)
    try:
        os.mkdir('XMLParser_Sonuc')
        sonucdosya.dosyadurumu = "yok"

    except FileExistsError:
        print('------->File alreeady exists')
        sonucdosya.dosyadurumu = "var"
        pass
    os.chdir(currentDirectory)


def dosyaexistcheck():
    currentDirectory = os.getcwd()
    desktopPath = os.path.join(os.environ["HOMEPATH"], "Desktop")
    os.chdir(desktopPath)
    try:
        os.mkdir('İthalatConverter')
        dosyaexistcheck.dosyadurumu = "yok"

    except FileExistsError:
        print('------->File alreeady exists')
        dosyaexistcheck.dosyadurumu = "var"
        pass
    os.chdir(currentDirectory)


excel_writer()
writer = excel_writer.writer
print(writer)
