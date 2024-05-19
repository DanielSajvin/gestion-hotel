from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.huesped import Huesped

class ModeloHuesped():
    def __init__(self) -> None:
        self.modeloHuesped = Huesped()
        
    
    def listarHuesped(self, tabla):
        table = tabla
        cocina = self.modeloHuesped.\
            obtenerHuesped()
        table.setRowCount(0)
        for row_number, row_data in enumerate(cocina):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
    def actuaizarHuesped(self, tabla):
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
                self.modeloHuesped.ActualizarHuesped(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5])

        self.listarHuesped(tabla)
        
    def CrearHuesped(self, nombre, dpi, anticipo, entrada, salida, table):
        if nombre and dpi and anticipo and entrada and salida:
            self.modeloHuesped.insertarHuesped(nombre, dpi, anticipo, entrada, salida)
            
            self.listarHuesped(table)
            
    def eliminarHueped(self, tabla):
        table = tabla
        if table.currentItem() != None:
            cod = table.currentItem().text()
            prov = self.modeloHuesped.obtenerHuespedCod(cod)
            if prov:
                self.modeloHuesped.eliminarHuesped(cod)
        self.listarHuesped(table)


    def onteneridhuespedporNombre(self, nombrehuesped):
        huesped = self.modeloHuesped.obteneidhuespedporNombre(nombrehuesped)
        return huesped[0]
