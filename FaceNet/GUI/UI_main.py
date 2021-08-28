import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from os import system

class ejecuta_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UserInterface.ui", self)
        #self.actCerradura.setEnabled(False)
        self.registroUsr.clicked.connect(self.usrRegistrar)

    def usrRegistrar(self):
        self.actCerradura.setEnabled(False)
        self.showRes.setText("Activando Usuario. Por favor espere...")
        system("python camera.py --first_name Name --last_name LastName --maxFileNumber 10")
        self.actCerradura.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ejecuta_GUI()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
