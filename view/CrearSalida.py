from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtWidgets
from modelos.control_Salida import ModeloRegistro
from modelos.control_huesped import ModeloHuesped
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog,QTableWidgetItem

import datetime

# Cargar la interfaz de usuario de CrearNivel.ui
Ui_CrearNivel, _ = loadUiType('view/CrearSalida.ui')


class CrearSalida(QMainWindow, Ui_CrearNivel):
    def __init__(self, tablah, tablafactura, num, *args, **kwargs):
        self.table = tablah
        self.tablefactura = tablafactura
        self.numero = num
        self.Modelo = ModeloRegistro()
        self.huesped = ModeloHuesped()
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.btn_cerrar.clicked.connect(self.close_event)
        self.btn_guardar.clicked.connect(self.guardarNiv)

        self.mostrarDatos()

    def mostrarDatos(self):
        datos_habitaciones = self.Modelo.datosporHabitacion(self.numero)



        if datos_habitaciones:
            habitacion_data = datos_habitaciones[0]  # Tomamos solo la primera fila de resultado

            idhabitacion = self.Modelo.opteneridpornumero(habitacion_data[0])

            if idhabitacion:
                habitacion_dataid = idhabitacion[0]

                id = habitacion_dataid[0]

            # Configurar los labels con los datos correspondientes
            self.lnl_numeroHabitacion.setText(f"No. Habitación: {habitacion_data[0]}")
            self.lbl_categoria.setText(f"Categoría: {habitacion_data[1]}")
            self.lbl_detalle.setText(f"Detalles: {habitacion_data[2]}")
            self.lbl_condicion.setText(f"Condición: {habitacion_data[3]}")
            self.lbl_precio.setText(f"Precio: {habitacion_data[4]}")
            self.lnl_Cliente.setText(f"Nombre del Cliente: {habitacion_data[5]}")
            self.lnl_DPI.setText(f"DPI: {habitacion_data[6]}")
            self.lnl_Razon.setText(f"Razón de Visita: {habitacion_data[7]}")
            self.lnl_FechaEntrada.setText(f"Fecha de Entrada: {habitacion_data[8]}")



            # Bloquear los labels para que no se puedan editar
            self.lnl_numeroHabitacion.setEnabled(False)
            self.lbl_categoria.setEnabled(False)
            self.lbl_detalle.setEnabled(False)
            self.lbl_condicion.setEnabled(False)
            self.lbl_precio.setEnabled(False)
            self.lnl_Cliente.setEnabled(False)
            self.lnl_DPI.setEnabled(False)
            self.lnl_Razon.setEnabled(False)
            self.lnl_FechaEntrada.setEnabled(False)


            costoAlojamiento  = self.Modelo.costoAlojamiento(id, habitacion_data[8])
            print(costoAlojamiento)
            listacosto = costoAlojamiento[0]
            table = self.tablaAlojamiento
            table.setRowCount(0)
            for row_number, row_data in enumerate(costoAlojamiento):
                table.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

            totalAlojamiento = listacosto[2]
            totalAlojamiento = str(totalAlojamiento)
            self.lbl_Total.setText(f"Total: {totalAlojamiento}")

        else:
            # Si no se encontraron datos, se puede mostrar un mensaje o realizar alguna otra acción
            print("No se encontraron datos para la habitación:", self.numeroHabitacion)



    def guardarNiv(self):
        nombreh = self.lnl_Cliente.text()
        partes = nombreh.split(": ")

        # Seleccionar la segunda parte y eliminar espacios en blanco
        nombre_cliente = partes[1].strip()
        print(nombre_cliente)
        fecha_actual = datetime.date.today()
        usuario_id = 1
        huesped_id = self.huesped.onteneridhuespedporNombre(nombre_cliente)
        print(huesped_id)
        self.Modelo.CrearFactura(fecha_actual, 1, huesped_id)

        self.Modelo.listarFactura(self.tablefactura)
        self.Modelo.updateFactura(self.tablefactura)

        facturaId = self.Modelo.ultimaFacutraId()
        extrasId = None
        idDetalle = self.Modelo.ultimoDetalleFactura()

        print(facturaId)
        print(extrasId)

        self.Modelo.updateDetalleFactura(fecha_actual, extrasId, facturaId, idDetalle)

        self.close_event()

    def close_event(self):
        self.close()
