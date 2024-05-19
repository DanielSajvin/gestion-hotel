from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from modelos.control_Categoria import ModeloCategoria
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog


# Cargar la interfaz de usuario de CrearNivel.ui
Ui_CrearNivel, _ = loadUiType('view/CrearCategoria.ui')


class CrearCategoria(QMainWindow, Ui_CrearNivel):
    def __init__(self, tabla, *args, **kwargs):
        self.table = tabla
        self.Modelo = ModeloCategoria()
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.btn_guardar.clicked.connect(self.guardarCat)
        self.btn_cerrar.clicked.connect(self.close_event)

    def guardarCat(self):
        nombre = self.lnl_1.text()
        precio = self.lnl_2.text()

        if not nombre or not precio:
            print("El número o nombre está vacío")
        else:
            self.Modelo.CrearCategoria(nombre, precio)
            self.Modelo.listarCategoria(self.table)
            self.close_event()

    def close_event(self):
        self.close()

