from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.usuario import Usuario

class ModeloUsuario():
    def __init__(self) -> None:
        self.modeloUsuario = Usuario()
        
    def listarUsuario(self, tabla):
        table = tabla
        usuarios = self.modeloUsuario.obtener_usuairo()
        table.setRowCount(0)
        for row_number, row_data in enumerate(usuarios):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 3:  # Columna que contiene el tipo de usuario
                    tipo_usuario = "Gerente" if data == 1 else "Empleado"
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(tipo_usuario))
                else:
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def actualizarUsuario(self, tabla):
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
                self.modeloUsuario.ActualizarUsuario(prod[0], prod[1], prod[2])


        self.listarUsuario(tabla)
        
    def CrearUsuario(self, nombre, usuario, contrasenia, tipo, table):
        if nombre and usuario and contrasenia and tipo:
            self.modeloUsuario.InsertarUsuario(nombre, usuario, contrasenia, tipo)
            self.listarUsuario(table)
            
            
    def eliminarUsuario(self, tabla):
        table = tabla
        if table.currentItem() != None:
            cod = table.currentItem().text()
            prov = self.modeloUsuario.obtenerUsuarioCod(cod)
            if prov:
                self.modeloUsuario.eliminarUsuario(cod)
        self.listarUsuario(table)
