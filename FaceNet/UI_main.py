import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from os import system


class ejecuta_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UserInterface.ui", self)

        self.showRes.setText("Seleccione una opción.")

        self.nombre.setVisible(False)
        self.apellido.setVisible(False)
        self.etiqNombre.setVisible(False)
        self.etiqApellido.setVisible(False)
        self.save.setVisible(False)
        self.registroUsr.clicked.connect(self.usrRegistrar)

    def usrRegistrar(self):
        self.showRes.setText("Por favor inserte su nombre y apellido")

        self.registroUsr.setVisible(False)
        self.actCerradura.setVisible(False)
        self.save.setVisible(True)
        self.nombre.setVisible(True)
        self.apellido.setVisible(True)
        self.etiqNombre.setVisible(True)
        self.etiqApellido.setVisible(True)

        self.save.clicked.connect(self.usrActivar)

    def usrActivar(self):
        self.showRes.setText("Activando Usuario. Por favor espere...")

        nombre = self.nombre.toPlainText()
        apellido = self.apellido.toPlainText()

        if nombre == "":
            self.showRes.setText("Favor de ingresar su nombre")
        elif apellido == "":
            self.showRes.setText("Favor de ingresar su apellido")
        else:
            self.showRes.setText("Activando Usuario. Por favor espere...")

            comando = "python camera.py --first_name " + nombre + " --last_name " + apellido + " --maxFileNumber 10"
            system(comando)
            system("python prepare_data.py")

            self.nombre.setPlainText("")
            self.apellido.setPlainText("")

            self.actCerradura.setVisible(True)
            self.registroUsr.setVisible(True)
            self.save.setVisible(False)
            self.nombre.setVisible(False)
            self.apellido.setVisible(False)
            self.etiqNombre.setVisible(False)
            self.etiqApellido.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ejecuta_GUI()

    MainWindow.show()
    sys.exit(app.exec())
