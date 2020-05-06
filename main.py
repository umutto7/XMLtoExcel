from PyQt5.QtWidgets import *
from GUI import Ui_mainwindow
import sys


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

    def Process(self,instance):
        file = self.ui.gelenlineEdit.text()
        print(file)
        self.ui.message.showMessage("Dönüştürme Başladı!!")

        self.progressdialog = QProgressDialog(self)
        self.progressdialog.setWindowTitle("Data Processing...")
        self.progressdialog.setLabelText("Data isleniyor...")
        self.progressdialog.setGeometry(500, 500, 500, 100)
        self.progressbar = QProgressBar(self)
        self.progressdialog.setBar(self.progressbar)
        self.progressdialog.resize(600, 100)
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)

        self.progressdialog.show()
        QApplication.processEvents()

        count = 5
        self.progressbar.setValue(count)





# bu kısmı araştır
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = PWC_Parser()
    pencere.show()
    sys.exit(app.exec_())
