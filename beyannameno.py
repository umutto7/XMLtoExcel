from xml.etree import cElementTree as ElementTree
import os, errno
import pandas as pd
from pandas import ExcelWriter


sonucpath = os.path.expanduser("~/Desktop/XML örneği/XML örneği/Sonuc")
filelistsonuc = os.listdir(sonucpath)
print(filelistsonuc)

sonuc_dict = {}


def beyannamenogetter(filelistsonuc,sonuc_dict):
    for filename in filelistsonuc:
        it = ElementTree.iterparse(filename)

        for _, el in it:
            el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
        root = it.root

        beyanname_no = root.find('Beyanname_no').text

        sonuc_dict[filename] = beyanname_no
    return sonuc_dict

beyannamenogetter(filelistsonuc,sonuc_dict)
print(sonuc_dict)