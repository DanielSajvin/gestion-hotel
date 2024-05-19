from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QTabWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from view.CrearNivel import CrearNivel
from view.CrearCategoria import CrearCategoria
from view.Crearhabitacion import CrearHabitacion
from modelos.control_cocina import ModeloCocina
from modelos.control_huesped import ModeloHuesped
from modelos.control_usuario import ModeloUsuario
from modelos.control_TipoUsuario import ModeloTipoUsuario
from modelos.control_habitacion import ModeloHabitacion
from modelos.control_nivel import ModeloNivel
from modelos.control_Categoria import ModeloCategoria
from modelos.control_hospedaje import ModeloHospedaje
import bcrypt

Ui_MainWindow, QMainWindow = loadUiType('view/interfaz.ui')


class Main_menuPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self, user, main_login) -> None:
        self.ModeloUsuario = ModeloUsuario()
        self.ModeloTipoUsuario = ModeloTipoUsuario()
        self.ModeloCocina = ModeloCocina()
        self.ModeloHuesped = ModeloHuesped()
        self.ModeloHabitacion = ModeloHabitacion()
        self.ModeloNivel = ModeloNivel()
        self.ModeloCategoria = ModeloCategoria()
        self.ModeloHospedaje = ModeloHospedaje()


        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # ********************************* saber que usuario esta en el programa *******************************
        self.usuario = self.ModeloUsuario.regresarUsuario(user)

        self.tipo_usuario = self.usuario[4]
        self.id_usuario = self.usuario[0]

        # Listar todas las tablas
        self.ModeloNivel.listarNivel(self.tablaNivel)
        self.ModeloHabitacion.listarHabitacion(self.tablaHabitacion)
        self.ModeloCategoria.listarCategoria(self.tablaCategoria)

        # ---------Estos botones son para asignar el nombre a los niveles y saber cuantos
        #  hay para colocar ese numero de pestañas-----------------------------
        self.actualizar_paneles_y_botones(self.tablaNivel)
        self.btn_habitacion.clicked.connect(lambda: self.actualizar_paneles_y_botones(self.tablaNivel))
        self.btn_actualizarH_2.clicked.connect(self.actualizarBotonesHabitacion)

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

        # --------------------------------- Botones Usuario ----------------------------------

        self.btn_register_6.clicked.connect(self.registrar)
        self.btn_register_6.clicked.connect(self.limpiar_labels_register)
        self.btn_listar_u.clicked.connect(lambda: self.ModeloUsuario.listarUsuario(self.tabla_usuario))
        self.btn_eliminar_u.clicked.connect(lambda: self.ModeloUsuario.eliminarUsuario(self.tabla_usuario))
        self.btn_actualizar_u.clicked.connect(lambda: self.ModeloUsuario.actualizarUsuario(self.tabla_usuario))
        self.btn_tipoUsuario.clicked.connect(self.mostrar_pagina_tipoUsuario)
        self.btn_usuario.clicked.connect(lambda: self.ModeloUsuario.listarUsuario(self.tabla_usuario))

        # ----------------------------------- Botones Tipo Usuario ----------------------------

        self.btn_volver.clicked.connect(self.mostrar_pagina_usuario)
        self.btn_listar_Tipo.clicked.connect(lambda: self.ModeloTipoUsuario.listarTipoUsuario(self.tabla_tipo_usuario))
        self.btn_eliminarTipo.clicked.connect(
            lambda: self.ModeloTipoUsuario.eliminarTipoUsuario(self.tabla_tipo_usuario))
        self.btn_actualizarTipo.clicked.connect(
            lambda: self.ModeloTipoUsuario.actualizarTipoUsuario(self.tabla_tipo_usuario))
        self.btn_crear_tipo.clicked.connect(
            lambda: self.ModeloTipoUsuario.CrearTipoUsuario(self.lnx_tipoUsusario.text(),
                                                            self.tabla_tipo_usuario))


        # -------------------------------------------------- Botones Habbitacion --------------------
        self.agre_piso.clicked.connect(self.agregar_planta)

        # --------------------------------------------- Botones de Nivel -----------------------------
        self.btn_crearNiv.clicked.connect(self.pg_CrearNiv)
        self.btn_crearNiv.clicked.connect(self.agregar_planta)

        # ---------------------------------------------- Botones de Categoria -----------------------
        self.btn_crearCat.clicked.connect(self.pg_CrearCat)

        # ------------------------------------------- Botones de habitacion -------------------------
        self.btn_crearHab.clicked.connect(self.pg_CrearHabitacion)

    def actualizarBotonesHabitacion(self):
        # Limpiar los botones existentes
        self.clearBotonesHabitacion()

        # Obtener datos de las habitaciones
        habitaciones = self.ModeloHabitacion.obtenerDatosHabitacionInterfaz()

        # Obtener la lista de IDs de habitaciones ocupadas
        ids_habitaciones_ocupadas = self.ModeloHospedaje.obtenerIdsHabitacionesOcupadas()

        # Obtener el índice de la pestaña actual en tab_recepcion
        indice_pestaña_actual = self.tab_recepcion.currentIndex()

        # Obtener el widget de la pestaña actual
        widget_pestaña_actual = self.tab_recepcion.widget(indice_pestaña_actual)

        # Obtener el layout del widget de la pestaña actual
        layout_pestaña_actual = widget_pestaña_actual.layout()

        # Crear botones de habitación para cada habitación y agregarlos al layout de la pestaña actual
        for habitacion in habitaciones:
            estado = habitacion[2]
            # Determinar el estado del botón según el estado de la habitación
            if estado == "ocupado":
                estado_boton = "Ocupado"
            else:
                estado_boton = "Libre"

            # Crear un botón para la habitación con su número, tipo y estado
            button = QPushButton(f"Habitación {habitacion[0]}\nTipo: {habitacion[1]}\nEstado: {estado_boton}")
            # Conectar el botón a la función pg_CrearHospedamiento con el número de habitación correspondiente
            button.clicked.connect(lambda _, num=habitacion[0]: self.pg_CrearHospedamiento(num))
            layout_pestaña_actual.addWidget(button)

    def clearBotonesHabitacion(self):
        # Obtener el índice de la pestaña actual en tab_recepcion
        indice_pestana_actual = self.tab_recepcion.currentIndex()

        # Obtener el widget de la pestaña actual
        widget_pestana_actual = self.tab_recepcion.widget(indice_pestana_actual)

        # Obtener el layout del widget de la pestaña actual
        layout_pestana_actual = widget_pestana_actual.layout()

        # Eliminar todos los widgets del layout de la pestaña actual
        for i in reversed(range(layout_pestana_actual.count())):
            widget = layout_pestana_actual.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()


    def actualizar_paneles_y_botones(self, tabla):
        # Obtener el número de niveles desde la base de datos
        numero_de_niveles = self.obtener_numero_de_niveles_desde_bd(tabla)

        # Limpiar pestañas
        self.tab_recepcion.clear()

        # Crear un diccionario para mapear los niveles a las habitaciones correspondientes
        habitaciones_por_nivel = {}

        # Obtener datos de las habitaciones
        self.ModeloHabitacion.updatehabitacion(self.tablaHabitacion)
        habitaciones = self.ModeloHabitacion.obtenerDatosHabitacionInterfaz()

        # Agrupar las habitaciones por nivel
        for habitacion in habitaciones:
            nivel = habitacion[3]
            if nivel not in habitaciones_por_nivel:
                habitaciones_por_nivel[nivel] = []
            habitaciones_por_nivel[nivel].append(habitacion)

        # Crear pestañas y botones de habitación para cada nivel
        for nivel in range(1, numero_de_niveles + 1):
            # Crear una pestaña para el nivel actual
            tab = QWidget()
            layout = QVBoxLayout()

            # Obtener las habitaciones para el nivel actual
            habitaciones_nivel = habitaciones_por_nivel.get(f"Nivel {nivel}", [])

            # Crear botones de habitación para el nivel actual
            for habitacion in habitaciones_nivel:
                estado = habitacion[2]
                # Verificar si la habitación está asociada al cliente y actualizar el estado

                button = QPushButton(f"Habitación {habitacion[0]}\nTipo: {habitacion[1]}\nEstado: {estado}")
                if estado == "Ocupado":
                    button.setEnabled(False)
                else:
                # Conecta la señal clicked del botón a la función pg_CrearHospedamiento con el número de habitación correspondiente
                    button.clicked.connect(lambda _, num=habitacion[0]: self.pg_CrearHospedamiento(num))
                layout.addWidget(button)

            # Establecer el diseño en la pestaña y agregarla al QTabWidget
            tab.setLayout(layout)
            self.tab_recepcion.addTab(tab, f"Nivel {nivel}")

        # Actualizar la interfaz gráfica
        self.tab_recepcion.setCurrentIndex(0)

    def agregar_planta(self):
        # Determina el nombre de la nueva planta
        planta_name = f"Piso {self.tab_recepcion.count() + 1}"
        planta_widget = QWidget()
        planta_layout = QVBoxLayout()
        planta_widget.setLayout(planta_layout)

        # Layout para los botones de habitaciones en la nueva pestaña
        planta_habitaciones_layout = QVBoxLayout()
        planta_layout.addLayout(planta_habitaciones_layout)

        # Botón para agregar habitación en la nueva pestaña
        add_btn = QPushButton("Agregar Habitación")
        add_btn.clicked.connect(lambda: self.agregar_habitacion(planta_habitaciones_layout))
        planta_layout.addWidget(add_btn)

        self.tab_recepcion.addTab(planta_widget, planta_name)

        # Cambia el nombre de la nueva pestaña
        self.tab_recepcion.setTabText(self.tab_recepcion.count() - 1, planta_name)

    def obtener_numero_de_niveles_desde_bd(self, tabla):
        self.ModeloNivel.updateNivel(tabla)
        numero_niveles = self.ModeloNivel.numeroNivel()
        return numero_niveles

    def pg_CrearHabitacion(self):
        self.crearHabitacionWindow = CrearHabitacion(self.tablaHabitacion)
        self.crearHabitacionWindow.show()

    def pg_CrearCat(self):
        self.crearCategoriaWindow = CrearCategoria(self.tablaCategoria)
        self.crearCategoriaWindow.show()

    # Metodo para conencta pestañas
    def pg_CrearNiv(self):
        # Instanciar y mostrar la ventana CrearNivel, pasando self como el padre
        self.crear_nivel_window = CrearNivel(self.tablaNivel)
        self.crear_nivel_window.show()

    def registrar(self):
        nombre = self.lnx_1nombre_2.text()
        user = self.lnx_usuario_2.text()
        cargo = self.cb_min_2.currentText()
        pw = self.lnx_password_3.text()
        pw_confirm = self.lnx_confirm_password_2.text()

        if pw == pw_confirm:
            pw = str(pw)

            salt = bcrypt.gensalt()

            # Encripta la contraseña del usuario
            hashed_password = bcrypt.hashpw(pw.encode('utf-8'), salt)
            if cargo == "Gerente":
                self.ModeloUsuario.CrearUsuario(nombre, user, hashed_password, 1, self.tabla_usuario)
            elif cargo == "Empleado":
                self.ModeloUsuario.CrearUsuario(nombre, user, hashed_password, 2, self.tabla_usuario)
            # Insertar la contraseña segura como una cadena de texto en la base de datos


        else:
            print("las contraseñas no coinciden")

    def limpiar_labels_register(self):
        self.lnx_1nombre_2.clear()
        self.lnx_confirm_password_2.clear()
        self.lnx_password_3.clear()
        self.lnx_usuario_2.clear()
