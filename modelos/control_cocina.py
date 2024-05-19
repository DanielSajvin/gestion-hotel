from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.cocina import Cocina

class ModeloCocina():
    def __init__(self) -> None:
        self.modeloCocina = Cocina()
        
    
    def listarAlimento(self, tabla):
        table = tabla
        cocina = self.modeloCocina.\
            obtener_alimento()
        table.setRowCount(0)
        for row_number, row_data in enumerate(cocina):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
    def actualizarAlimento(self, tabla):
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
                self.modeloCocina.ActualizarAlimento(prod[0], prod[1], prod[2], prod[3])

        self.listarAlimento(tabla)
        
    def CrearAlimento(self, nombre, fechaEntrada, fechaExpiracion, table):
        if nombre and fechaEntrada and fechaExpiracion:
            self.modeloCocina.insertarAlimento(nombre, fechaEntrada, fechaExpiracion)
            
            self.listarAlimento(table)
            
    def eliminarAlimento(self, tabla):
        table = tabla
        if table.currentItem() != None:
            cod = table.currentItem().text()
            prov = self.modeloCocina.obtenerAlimentoCod(cod)
            if prov:
                self.modeloCocina.eliminarAlimento(cod)
        self.listarAlimento(table)
