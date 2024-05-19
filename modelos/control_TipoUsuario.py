from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.tipoUsuario import TipoUsuario

class ModeloTipoUsuario():
    def __init__(self) -> None:
        self.modeloTipoUsuario = TipoUsuario()
        
    def listarTipoUsuario(self, tabla):
        table = tabla
        usuarios = self.modeloTipoUsuario.obtener_tipousuairo()
        table.setRowCount(0)
        for row_number, row_data in enumerate(usuarios):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def actualizarTipoUsuario(self, tabla):
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
                self.modeloTipoUsuario.ActualizarTipoUsuario(prod[0], prod[1])


        self.listarTipoUsuario(tabla)
        
    def CrearTipoUsuario(self, tipo, table):
        if tipo:
            self.modeloTipoUsuario.InsertarTipoUsuario(tipo)
            self.listarTipoUsuario(table)
            
            
    def eliminarTipoUsuario(self, tabla):
        table = tabla
        if table.currentItem() != None:
            cod = table.currentItem().text()
            prov = self.modeloTipoUsuario.obtenerUsuarioCod(cod)
            if prov:
                self.modeloTipoUsuario.eliminarTipoUsuario(cod)
        self.listarTipoUsuario(table)
