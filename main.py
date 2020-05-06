from PyQt5.QtWidgets import *
from GUI import Ui_mainwindow
import sys


class PWC_Parser(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)

    def findfile(self):

        filebrowser = QFileDialog.getOpenFileName(self, "Multiple Files", "~/Desktop", "*.xml")
        self.directory.setText(filebrowser[0])


# bu kısmı araştır
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = PWC_Parser()
    pencere.show()
    sys.exit(app.exec_())
