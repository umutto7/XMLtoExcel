from xml.etree import cElementTree as ElementTree
import os, errno
from pathlib import Path
import pandas as pd
from pandas import ExcelWriter
import timeit

# IGNORE ALL NAMESAPCES and get root of the XML
it = ElementTree.iterparse('Sonuc.xml')
for _, el in it:
    el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
root = it.root

# -----> ExcelWriter
writer = ExcelWriter('PythonExportSonuc.xlsx')

# XML SonuçGenel #

sonuc_headers = [elem.tag for elem in root]
sonuc_text = [elem.text for elem in root]
sonucgenel_table = dict(zip(sonuc_headers, sonuc_text))
df_sonucgenel = pd.DataFrame(sonucgenel_table, index=[0])
# df_sonucgenel.to_excel(writer,'Sonuc')


# -----> XML Belgeler kısmı

belgeler = root.find("Belgeler")
belge = belgeler.findall("Belge")

blg_headers = []
blg_hdr_count = 0
blg_count = 0

for item in belge:
    blgrow = []
    if blg_hdr_count == 0:
        for x in item.iter():
            a = x.tag
            blg_headers.append(a)
        blg_hdr_count += 1
    for y in item.iter():
        detay = y.text
        blgrow.append(detay)
    blg_dict = dict(zip(blg_headers, blgrow))
    if blg_count == 0:
        df_belge = pd.DataFrame(blg_dict, index=[0])
        blg_count += 1
    else:
        df_append = pd.DataFrame(blg_dict, index=[0])
        df_belge = df_belge.append(df_append)
# df_belge.to_excel(writer, 'Belgeler')

# -----> XML Vergiler kısmı

vergiler = root.find("Vergiler")
vergi = vergiler.findall("Vergi")
vrg_headers = []
vrg_hdr_count = 0
vrg_count = 0

for item in vergi:
    vergirow = []
    if vrg_hdr_count == 0:
        for x in item.iter():
            a = x.tag
            vrg_headers.append(a)
        vrg_hdr_count += 1
    for y in item.iter():
        detay = y.text
        vergirow.append(detay)
    vergi_dict = dict(zip(vrg_headers, vergirow))
    if vrg_count == 0:
        df_vergi = pd.DataFrame(vergi_dict, index=[0])
        vrg_count += 1
    else:
        df_append = pd.DataFrame(vergi_dict, index=[0])
        df_vergi = df_vergi.append(df_append)

# df_vergi.to_excel(writer, 'Vergiler')

# -----> XML ToplamVergiler kısmı

vergiler_toplam = root.find("Toplam_vergiler")
vergi_toplam = vergiler_toplam.findall("Toplam_Vergi")
topvrg_headers = []
topvrg_hdr_count = 0
topvrg_count = 0

for item in vergi_toplam:
    topvergirow = []
    if topvrg_hdr_count == 0:
        for x in item.iter():
            a = x.tag
            topvrg_headers.append(a)
        topvrg_hdr_count += 1
    for y in item.iter():
        detay = y.text
        topvergirow.append(detay)
    topvergi_dict = dict(zip(topvrg_headers, topvergirow))
    if topvrg_count == 0:
        df_vergitop = pd.DataFrame(topvergi_dict, index=[0])
        topvrg_count += 1
    else:
        df_append = pd.DataFrame(topvergi_dict, index=[0])
        df_vergitop = df_vergitop.append(df_append)

# df_vergi.to_excel(writer, 'Toplam_Vergi')

# -----> XML ToplananVergiler kısmı
vergiler_toplanan = root.find("Toplam_vergiler")
vergi_toplanan = vergiler_toplanan.findall("Toplam_Vergi")
toplnvrg_headers = []
toplnvrg_hdr_count = 0
toplnvrg_count = 0

for item in vergi_toplanan:
    toplnnvergirow = []
    if toplnvrg_hdr_count == 0:
        for x in item.iter():
            a = x.tag
            toplnvrg_headers.append(a)
        toplnvrg_hdr_count += 1
    for y in item.iter():
        detay = y.text
        toplnnvergirow.append(detay)
    toplnnvergi_dict = dict(zip(toplnvrg_headers, toplnnvergirow))
    if toplnvrg_count == 0:
        df_vergitoplnn = pd.DataFrame(toplnnvergi_dict, index=[0])
        toplnvrg_count += 1
    else:
        df_append = pd.DataFrame(toplnnvergi_dict, index=[0])
        df_vergitoplnn = df_vergitoplnn.append(df_append)
# df_vergitoplnn.to_excel(writer, 'ToplananVergiler')

# -----> XML Hesapdetayları kısmı
hesapdetay = root.find("Hesap_detaylari")
hesap = hesapdetay.findall("Hesap_detay")
hsp_headers = []
hsp_hdr_count = 0
hsp_count = 0

for item in hesap:
    hsprow = []
    if hsp_hdr_count == 0:
        for x in item.iter():
            a = x.tag
            hsp_headers.append(a)
        hsp_hdr_count += 1
    for y in item.iter():
        detay = y.text
        hsprow.append(detay)
    hsp_dict = dict(zip(hsp_headers, hsprow))
    if hsp_count == 0:
        df_hsp = pd.DataFrame(hsp_dict, index=[0])
        hsp_count += 1
    else:
        df_append = pd.DataFrame(hsp_dict, index=[0])
        df_hsp = df_hsp.append(df_append)
# df_hsp.to_excel(writer, 'HesapDetayları')
# -----> XML Özetbeyanbilgi kısmı

# -----> XML Gümrükkıymet kısmı

gumrukkıymetler = root.find("Gumruk_kiymetleri")
gumruk_kıymet = gumrukkıymetler.findall("Gumruk_Kiymeti")
kym_headers = []
kym_hdr_count = 0
kym_count = 0

for item in gumruk_kıymet:
    kym_row = []
    if kym_hdr_count == 0:
        for x in item.iter():
            a = x.tag
            kym_headers.append(a)
        kym_hdr_count += 1
    for y in item.iter():
        detay = y.text
        kym_row.append(detay)
    kym_dict = dict(zip(kym_headers, kym_row))
    if kym_count == 0:
        df_kym = pd.DataFrame(kym_dict, index=[0])
        kym_count += 1
    else:
        df_append = pd.DataFrame(kym_dict, index=[0])
        df_kym = df_kym.append(df_append)

print(df_kym)
# df_kym.to_excel(writer, 'GümrükKıymetleri')

# -----> XML İstatikikıymet kısmı

istatkıymetler = root.find("Istatistiki_kiymetleri")
istak_kıymet = istatkıymetler.findall("Istatistiki_Kiymeti")
ist_headers = []
ist_hdr_count = 0
ist_count = 0

for item in istak_kıymet:
    ist_row = []
    if ist_hdr_count == 0:
        for x in item.iter():
            a = x.tag
            ist_headers.append(a)
        ist_hdr_count += 1
    for y in item.iter():
        detay = y.text
        ist_row.append(detay)
    ist_dict = dict(zip(ist_headers, ist_row))
    if ist_count == 0:
        df_ist = pd.DataFrame(ist_dict, index=[0])
        ist_count += 1
    else:
        df_append = pd.DataFrame(ist_dict, index=[0])
        df_ist = df_ist.append(df_append)

print(df_ist)
# df_ist.to_excel(writer, 'İstatikikıymetleri')