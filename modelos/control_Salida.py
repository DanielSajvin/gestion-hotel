from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.salida import Registro
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


class ModeloRegistro:
    def __init__(self) -> None:
        self.modeloRegistro = Registro()

    def listarFactura(self, tabla):
        # Obtener datos de la base de datos
        factura = self.modeloRegistro.obtenerdatosFacturas()

        # Establecer el número de filas en la tabla
        tabla.setRowCount(len(factura))

        # Insertar los datos en la tabla
        for row_number, row_data in enumerate(factura):
            # Insertar datos en todas las columnas, incluida la primera columna
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                tabla.setItem(row_number, column_number, item)

            # Hacer la primera columna invisible
            tabla.setColumnHidden(0, True)
            tabla.setColumnHidden(1, True)
            tabla.setColumnHidden(2, True)

    def updateFactura(self, tabla):
        table = tabla
        products = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number, column_number) != None:
                    fila.append(table.item(row_number, column_number).text())
            if len(fila) > 0:
                products.append(fila)
            fila = []

        if len(products) > 0:
            for prod in products:
                self.modeloRegistro.updateFacturaRegistro(prod[3], prod[1], prod[2], prod[0])

        self.listarFactura(tabla)

    def datosporHabitacion(self, numeroH):
        datos = self.modeloRegistro.obtenerdatosporHabitacion(numeroH)
        return datos

    def CrearFactura(self, fecha, usuario_id, huesped_id):
        if fecha and usuario_id and huesped_id:
            self.modeloRegistro.crearFactura(fecha, usuario_id, huesped_id)
        else:
            print("Faltan datos para crear factura")

    def costoAlojamiento(self, idHabitacion, fechaE):
        datos = self.modeloRegistro.obtenerCostoAlojamiento(idHabitacion, fechaE)
        return datos

    def opteneridpornumero(self, numeroHabitacion):
        datos = self.modeloRegistro.obteneridporHabitacion(numeroHabitacion)
        return datos

    def ingresarFechaEntrada(self, fechaS, FechaE, subtotal, descuento, anticipo, total, idExtras, idHabitacion, idFactura):
        self.modeloRegistro.insertarFechaEntrada(fechaS, FechaE, subtotal, descuento, anticipo, total, idExtras, idHabitacion, idFactura)

    def updateDetalleFactura(self, fechaS, extrasId, facturaId, idDetalle):
        self.modeloRegistro.updateDetalleFactura(fechaS, extrasId, facturaId, idDetalle)

    def ultimaFacutraId(self):
        regresar = self.modeloRegistro.obtenerUltimoIdFactura()
        return regresar

    def ultimoDetalleFactura(self):
        reg = self.modeloRegistro.obtenerUltimoIdDetalleFactura()
        return reg
