from PyQt5.QtWidgets import *
from GUI import Ui_mainwindow
import sys,os
from gelenParse import gelen_parse
from sonucParse import sonuc_parse
from functions import gelendosya, sonucdosya, excel_writer, dosyaexistcheck
from pandas import ExcelWriter


class PWC_Parser(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)

        # Button for Gelen XML files
        self.ui.gelenlineEdit.setPlaceholderText("Donüştürülecek XML dosyası seçin!")
        self.ui.gelen_btn.clicked.connect(self.findfileGelen)

        # Button for Sonuç XML files
        self.ui.sonucLineEdit.setPlaceholderText("Donüştürülecek XML dosyası seçin!")
        self.ui.sonu_btn.clicked.connect(self.findfileSonuc)

        # Button for Process files
        self.ui.convert_btn.clicked.connect(self.Process)

    def findfileGelen(self):
        filebrowser = QFileDialog.getOpenFileName(self, "Multiple Files", "~/Desktop", "*.xml")
        self.ui.gelenlineEdit.setText(filebrowser[0])

    def findfileSonuc(self):
        filebrowser = QFileDialog.getOpenFileName(self, "Multiple Files", "~/Desktop", "*.xml")
        self.ui.sonucLineEdit.setText(filebrowser[0])

    def Process(self):

        errmsg = "Lutfen dosya uzantisini tekrar kontrol ediniz yanlis girilmistir!Dosya uzanıtısı seçtiğinizden emin olun!!!"

        gelenpath = self.ui.gelenlineEdit.text()
        if gelenpath is not None:
            if gelenpath == "" or "/" not in gelenpath or ".xml" in gelenpath or gelenpath.endswith('/') is False or gelenpath.startswith('C:') is False:
                self.message1 = QMessageBox.about(self, "Hatalı Dosya Uzantısı!!!", errmsg)

            filelistgelen = os.listdir(gelenpath)
            for filename in filelistgelen:
                if not filename.endswith('.xml'):
                    filelistgelen.remove(filename)
        else: pass

        sonucpath = self.ui.sonucLineEdit.text()
        if sonucpath is not None:
            if sonucpath == "" or "/" not in sonucpath or ".xml" in sonucpath or sonucpath.endswith('/') is False or sonucpath.startswith('C:') is False:
                self.message1 = QMessageBox.about(self, "Hatalı Dosya Uzantısı!!!", errmsg)

            filelistsonuc = os.listdir(sonucpath)
            for filename in filelistsonuc:
                if not filename.endswith('.xml'):
                    filelistsonuc.remove(filename)
        else: pass

        # ---------> initializing the sonuc xml beyanname no filename dict
        sonuc_dict = {}

        # ---------> initializing the ExcelWriter yarım kaldı!!
        excel_writer()
        writer = excel_writer.writer

        self.progressdialog = QProgressDialog(self)
        self.progressdialog.setWindowTitle("Data Processing...")
        self.progressdialog.setLabelText("Data isleniyor...")
        self.progressdialog.setGeometry(500, 500, 500, 100)
        self.progressbar = QProgressBar(self)
        self.progressdialog.setBar(self.progressbar)
        self.progressdialog.resize(600, 100)
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setStyleSheet("QProgressBar::chunk {background:orange}")

        self.progressdialog.show()
        QApplication.processEvents()

        # ---------> Gelen Dosya exist check
        self.ui.message.showMessage("Dönüştürme Başladı!")
        count = 5
        self.progressbar.setValue(count)
        gelendosya()
        if gelendosya.dosyadurumu == "var":
            self.message2 = QMessageBox.about(self, "Desktopu temizle!!!", errmsg)
        QApplication.processEvents()

        # ---------> Sonuç Dosya exist check
        count += 5
        self.progressbar.setValue(count)
        sonucdosya()
        if sonucdosya.dosyadurumu == "var":
            self.message2 = QMessageBox.about(self, "Desktopu temizle!!!", errmsg)
        QApplication.processEvents()

        count +=30
        self.progressbar.setValue(count)
        Gelen_Parse(filelistgelen)
        QApplication.processEvents()
        count += 10
        self.progressbar.setValue(count)



        count += 25
        self.progressbar.setValue(count)
        if sonucpath is not None:
            Sonuc_Parse(filelistsonuc)
        QApplication.processEvents()

        count += 25
        self.progressbar.setValue(count)

        if count == 100:
            self.progressdialog.close()
            self.message = QMessageBox.about(self, "TaxTech", "Data Donusturme Tamamlandi!")



# bu kısmı araştır
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = PWC_Parser()
    pencere.show()
    sys.exit(app.exec_())
