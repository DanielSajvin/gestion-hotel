# Codigo para saltarse el login
from view.menu_principal import Main_menuPrincipal
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


import sys
from PyQt5.QtWidgets import QApplication
from view.ventana_login import Main_login
# Comentario
Ui_MainWindow, QMainWindow = loadUiType('view/interfaz.ui')

app = QApplication(sys.argv)
# window = Main_menuPrincipal(QMainWindow, Ui_MainWindow)
window = Main_login()
window.show()


sys.exit(app.exec_())
