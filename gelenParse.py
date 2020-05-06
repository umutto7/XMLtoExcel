from xml.etree import cElementTree as ElementTree
import os, errno
from pathlib import Path
import pandas as pd
from pandas import ExcelWriter
import timeit

start = timeit.default_timer()

######## get desktop path

currentDirectory = os.getcwd()
# desktopPath = os.path.join(os.environ["HOMEPATH"], "Desktop")
# os.chdir(desktopPath)
try:
    os.mkdir('Gelen_Parser')
except FileExistsError:
    print('------->File alreeady exists')
    pass

gelen_path = os.path.join(currentDirectory, "Gelen_Parser")
#os.chdir(currentDirectory)

# IGNORE ALL NAMESAPCES and get root of the XML
it = ElementTree.iterparse('Gelen.xml')
for _, el in it:
    el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
root = it.root

# -----> ExcelWriter
writer = ExcelWriter('PythonExportGelen.xlsx')

# XML BeyannameBilgi #

beyanname_bilgi = root.find("BeyannameBilgi")

beyannamebilgi_headers = []
byncount = 0
byncount1 = 0
beyanname_csv = []

for item in beyanname_bilgi:
    a = item.tag
    beyannamebilgi_headers.append(a)
    b = item.text
    beyanname_csv.append(b)

beyanname_dict = dict(zip(beyannamebilgi_headers, beyanname_csv))
df_beyanname = pd.DataFrame(beyanname_dict, index=[0])


df_beyanname.to_excel(writer,'Beyanname')

# -----> XML Firma Bilgi

firmaBilgi = beyanname_bilgi.find("Firma_bilgi")
firmaBilgiler = firmaBilgi.findall("firma")

firma_headers = []
firma_headers_count = 0
firma_count = 0

for items in firmaBilgiler:
    firma_rows = []
    if firma_headers_count ==0:
        for x in items.iter():
            a = x.tag
            firma_headers.append(a)
        firma_headers_count += 1
    for item in items.iter():
        firma_detaylar = item.text
        firma_rows.append(firma_detaylar)
    firma_dict = dict(zip(firma_headers, firma_rows))
    if firma_count == 0:
        df_firma = pd.DataFrame(firma_dict, index=[0])
        firma_count = 1
    else:
        df_append = pd.DataFrame(firma_dict, index=[0])
        df_firma = df_firma.append(df_append)


df_firma.to_excel(writer,'FirmaBilgi')

#XML Teminat kısmı
# bu kısım boş soralım

teminatkısmı = beyanname_bilgi.find("Teminat")
#print(teminatkısmı)

#-----> Özetbeyanlar kısmı

ozetbeyanlar = beyanname_bilgi.find("Ozetbeyanlar")
ozetbeyanlar_line = ozetbeyanlar.find("Ozetbeyan")

ozetbeyan_headers = [elem.tag for elem in ozetbeyanlar_line.iter() if elem is not ozetbeyanlar_line]
ozetbeyan_row = [elem.text for elem in ozetbeyanlar_line.iter() if elem is not ozetbeyanlar_line]
ozetbeyan_table = dict(zip(ozetbeyan_headers, ozetbeyan_row))
df_ozetbeyan = pd.DataFrame(ozetbeyan_table, index=[0])

df_ozetbeyan.to_excel(writer,'Özetbeyanlar')


#-----> XML Kalem kısmı

kalemler = beyanname_bilgi.find("Kalemler")
kalem_lineitems =kalemler.findall("kalem")

kalemler_headers = []
kalem_hdr_count = 0
kalem_count = 0

for kalem in kalem_lineitems:
    kalemrow = []
    if kalem_hdr_count == 0:
        for x in kalem.iter():
            a = x.tag
            kalemler_headers.append(a)
        kalem_hdr_count += 1

    for y in kalem.iter():
        detaylar = y.text
        kalemrow.append(detaylar)
        # if y.tag == 'Kalem_sira_no':
        #     kalem_sıra_no = y.text
    aa = dict(zip(kalemler_headers, kalemrow))


    if kalem_count == 0:
        df_kalem = pd.DataFrame(aa, index=[0])
        kalem_count = 1
    else:
        df_append = pd.DataFrame(aa, index=[0])
        df_kalem = df_kalem.append(df_append)

df_kalem.to_excel(writer,'Kalem')


#-----> XML Sorular Cevaplar

sorucevap = beyanname_bilgi.find("Sorular_cevaplar")
sorucevap_line = sorucevap.findall("Soru_Cevap")

sc_headers = []
sc_headers_count = 0
sc_count = 0

for sorucevap in sorucevap_line:
    sc_row = []
    if sc_headers_count == 0:
        for x in sorucevap.iter():
            a = x.tag
            sc_headers.append(a)
        sc_headers_count += 1
    for item in sorucevap.iter():
        sc_detaylar = item.text
        sc_row.append(sc_detaylar)
    sc_dict = dict(zip(sc_headers, sc_row))
    if sc_count == 0:
        df_sc = pd.DataFrame(sc_dict, index=[0])
        sc_count = 1
    else:
        df_append = pd.DataFrame(sc_dict, index=[0])
        df_sc = df_sc.append(df_append)

df_sc.to_excel(writer,'SorularCevaplar')

#-----> XML Dokümanlar

dokuman = beyanname_bilgi.find("Dokumanlar")
dok_li = dokuman.findall("Dokuman")
dok_headers = []
dok_headers_count = 0
dok_count = 0

for dok in dok_li:
    dok_rows = []
    if dok_headers_count == 0:
        for doc in dok.iter():
            a = doc.tag
            dok_headers.append(a)
        dok_headers_count += 1
    for doc in dok.iter():
        doc_detaylar = doc.text
        dok_rows.append(doc_detaylar)
    dok_dict = dict(zip(dok_headers, dok_rows))
    if dok_count == 0:
        df_dokuman = pd.DataFrame(dok_dict, index=[0])
        dok_count = 1
    else:
        df_append = pd.DataFrame(dok_dict, index=[0])
        df_dokuman = df_dokuman.append(df_append)

df_dokuman.to_excel(writer,'Dokümanlar')


#-----> XML vergiler

vergiler = beyanname_bilgi.find("Vergiler")
vergi_lineitems = vergiler.findall("Vergi")

vergi_headers = []
vergi_headers_count = 0
vergi_count = 0

for vergi in vergi_lineitems:
    vergi_rows = []
    if vergi_headers_count == 0:
        for x in vergi.iter():
            a = x.tag
            vergi_headers.append(a)
        vergi_headers_count += 1
    for item in vergi.iter():
        vergi_detaylar = item.text
        vergi_rows.append(vergi_detaylar)
    vergi_dict = dict(zip(vergi_headers, vergi_rows))
    if vergi_count == 0:
        df_vergi = pd.DataFrame(vergi_dict, index=[0])
        vergi_count = 1
    else:
        df_append = pd.DataFrame(vergi_dict, index=[0])
        df_vergi = df_vergi.append(df_append)

df_vergi.to_excel(writer, 'Vergiler')


#-----> XML Kıymetkalem

kıymetbildirim = beyanname_bilgi.find("KiymetBildirim")
kıymet = kıymetbildirim.find("Kiymet")

kıy_headers_1 = [elem.tag for elem in kıymet if elem is not kıymet]
kıy_rows_1 = [elem.text for elem in kıymet if elem is not kıymet]
kıymet1_table = dict(zip(kıy_headers_1, kıy_rows_1))
df_kıymet1 = pd.DataFrame(kıymet1_table, index=[0])


kıy_kalem = kıymet.find("KiymetKalemler")
kıymet_kalem = kıy_kalem.findall("KiymetKalem")

kıy_headers2 = []
kıy_headers_count = 0
kıymet_count = 0
for kıymet in kıymet_kalem:
    kıymet_rows = []
    if kıy_headers_count == 0:
        for kıy in kıymet.iter():
            a = kıy.tag
            kıy_headers2.append(a)
        kıy_headers_count += 1
    for kıy in kıymet.iter():
        kıy_detaylar = kıy.text
        kıymet_rows.append(kıy_detaylar)
    kıymet_dict = dict(zip(kıy_headers2, kıymet_rows))
    if kıymet_count == 0:
        df_kıymet = pd.DataFrame(kıymet_dict, index=[0])
        kıymet_count = 1
    else:
        df_append = pd.DataFrame(kıymet_dict, index=[0])
        df_kıymet = df_kıymet.append(df_append)

df_kıymet.to_excel(writer, 'KıymetBildirim')
writer.save()



#table_kalem_vergi = pd.merge(df_kalem, df_vergi, left_on='Kalem_sira_no', right_on='Kalem_no', how='left', sort=False)

# file_name = 'Pwc.csv';
# table_kalem_vergi.to_csv(file_name)

####### timer
stop = timeit.default_timer()
print('Time: ', stop - start)

