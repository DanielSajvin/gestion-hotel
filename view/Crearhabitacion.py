from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from modelos.control_habitacion import ModeloHabitacion
from controladores.nivel import RegistrarNivel
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog
from PyQt5.QtWidgets import QMessageBox


# Cargar la interfaz de usuario de CrearNivel.ui
Ui_CrearNivel, _ = loadUiType('view/CrearHabitacion.ui')


class CrearHabitacion(QMainWindow, Ui_CrearNivel):
    def __init__(self, tabla, *args, **kwargs):
        self.table = tabla
        self.ModeloHabitacion = ModeloHabitacion()
        self.modeloNivel = RegistrarNivel()
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)


        self.lnl_precio.setReadOnly(True)

        self.btn_cerrar.clicked.connect(self.close_event)
        self.btn_guardar.clicked.connect(self.guardarNiv)
        self.datosNivelHabitacion()
        self.datosCategoriaHabitacion()
        self.seleccionCategoria.currentIndexChanged.connect(self.actualizarPrecio)

    def datosNivelHabitacion(self):
        nNivel = self.modeloNivel.obtenerNombreNivel()
        self.niveles_dict = {}  # Diccionario para mapear nombres de niveles a IDs
        self.seleccionNivel.clear()
        self.seleccionNivel.addItem("Selecciona Nivel")
        for nivel in nNivel:
            id_nivel = nivel[0]  # Obtener el ID del nivel
            nombre_nivel = nivel[1]  # Obtener el nombre del nivel
            self.niveles_dict[nombre_nivel] = id_nivel  # Mapear nombre a ID
            self.seleccionNivel.addItem(nombre_nivel)

    def datosCategoriaHabitacion(self):
        nCategoria = self.modeloNivel.obtenerNombreCategoria()
        self.categoria_dict = {}  # Diccionario para mapear nombres de niveles a IDs
        self.precio_categoria_dict = {}  # Diccionario para mapear nombres de categorías a precios
        self.seleccionCategoria.clear()
        self.seleccionCategoria.addItem("Selecciona Categoria")
        for categoria in nCategoria:
            id_categoria = categoria[0]  # Obtener el ID de la categoría
            nombre_categoria = categoria[1]  # Obtener el nombre de la categoría
            precio_categoria = categoria[2]  # Obtener el precio de la categoría
            self.categoria_dict[nombre_categoria] = id_categoria  # Mapear nombre a ID
            self.precio_categoria_dict[nombre_categoria] = precio_categoria  # Mapear nombre a precio
            self.seleccionCategoria.addItem(nombre_categoria)

    def guardarNiv(self):
        numeroNivel = self.lnl_numeroH.text()
        detalle = self.lnl_detalles.text()
        nombre_nivel = self.seleccionNivel.currentText()  # Obtener el nombre seleccionado del ComboBox
        id_nivel = int(self.niveles_dict.get(nombre_nivel))  # Obtener el ID correspondiente al nombre seleccionado
        nombre_categoria = self.seleccionCategoria.currentText()
        id_categoria = int(self.categoria_dict.get(nombre_categoria))
        estado = 1

        # Obtener el precio de la categoría seleccionada



        # Verificar que todos los campos estén llenos y que se haya seleccionado una opción válida en los ComboBox
        if not numeroNivel or not detalle or nombre_nivel == "Selecciona Nivel" or nombre_categoria == "Selecciona Categoria":
            # Mostrar una alerta indicando que falta llenar los campos
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setWindowTitle("Error")
            alerta.setText(
                "Por favor, completa todos los campos del formulario y selecciona una opción válida en los ComboBox.")
            alerta.exec_()
            return  # No hacer nada más si falta información

        # Si se ha seleccionado una opción válida, establecer el precio en el LineEdit de precio

        # Si todos los campos están llenos y se ha seleccionado una opción válida, guardar los datos
        self.ModeloHabitacion.CrearHabitacion(numeroNivel, detalle, id_categoria, id_nivel, estado)
        self.ModeloHabitacion.listarHabitacion(self.table)
        self.close_event()

    def actualizarPrecio(self, index):
        nombre_categoria = self.seleccionCategoria.currentText()
        precio_categoria = self.precio_categoria_dict.get(nombre_categoria)
        self.lnl_precio.setText(str(precio_categoria))

    def close_event(self):
        self.close()
