from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QTabWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from modelos.control_cocina import ModeloCocina
from modelos.control_huesped import ModeloHuesped

Ui_MainWindow, QMainWindow = loadUiType('view/interfaz.ui')


class Main_menuPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self, user, main_login) -> None:
        self.ModeloCocina = ModeloCocina()
        self.ModeloHuesped = ModeloHuesped()

        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # -------------------------- Botones Cocina ------------------------------------------

        self.btn_listar.clicked.connect(lambda: self.ModeloCocina.listarAlimento(self.tabla_cocina))
        self.btn_eliminar_c.clicked.connect(lambda: self.ModeloCocina.eliminarAlimento(self.tabla_cocina))
        self.btn_actualizar_c.clicked.connect(lambda: self.ModeloCocina.actualizarAlimento(self.tabla_cocina))
        self.btn_agregar_c.clicked.connect(lambda: self.ModeloCocina.CrearAlimento(self.lnl_producto.text(),
                                                                                   self.lnl_entrada.text(),
                                                                                   self.lnl_vencimiento.text(),
                                                                                   self.tabla_cocina))

        # ------------------------------------------- Botones huesped ------------------------------
        self.btn_listarH.clicked.connect(lambda: self.ModeloHuesped.listarHuesped(self.tablaHuesped))
        self.btn_eliminarH.clicked.connect(lambda: self.ModeloHuesped.eliminarHueped(self.tablaHuesped))
        self.btn_actualizarH.clicked.connect(lambda: self.ModeloHuesped.actuaizarHuesped(self.tablaHuesped))
        self.btn_ingresarH.clicked.connect(lambda: self.ModeloHuesped.CrearHuesped(self.lnl_nombreH.text(),
                                                                                   self.lnl_dpiH.text(),
                                                                                   float(self.lnl_anticipo.text()),
                                                                                   self.lnl_entradaH.text(),
                                                                                   self.lnl_salidaH.text(),
                                                                                   self.tablaHuesped))
