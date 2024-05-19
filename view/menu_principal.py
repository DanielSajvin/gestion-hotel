from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QTabWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from modelos.control_cocina import ModeloCocina

Ui_MainWindow, QMainWindow = loadUiType('view/interfaz.ui')


class Main_menuPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self, user, main_login) -> None:
        self.ModeloCocina = ModeloCocina()

        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
