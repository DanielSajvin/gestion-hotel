from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from modelos import ModeloNivel
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog


# Cargar la interfaz de usuario de CrearNivel.ui
Ui_CrearNivel, _ = loadUiType('view/CrearNivel.ui')


class CrearNivel(QMainWindow, Ui_CrearNivel):
    def __init__(self, tabla, *args, **kwargs):
        self.table = tabla
        self.ModeloNivel = ModeloNivel()
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.btn_cerrar.clicked.connect(self.close_event)
        self.btn_GuardarNiv.clicked.connect(self.guardarNiv)

    def guardarNiv(self):
        numeroNivel = self.lnl_NoNiv.text()
        nombreNivel = self.lnl_NombreNiv.text()

        if not numeroNivel or not nombreNivel:
            print("El número o nombre está vacío")
        else:
            self.ModeloNivel.CrearNivel(nombreNivel, numeroNivel)
            self.ModeloNivel.listarNivel(self.table)
            self.close_event()

    def close_event(self):
        self.close()


