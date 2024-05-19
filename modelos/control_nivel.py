from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.nivel import RegistrarNivel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


class ModeloNivel:
    def __init__(self) -> None:
        self.modeloNivel = RegistrarNivel()

    def listarNivel(self, tabla):
        # Obtener datos de la base de datos
        cocina = self.modeloNivel.obtenerNivel()

        # Establecer el número de filas en la tabla
        tabla.setRowCount(len(cocina))

        # Insertar los datos en la tabla
        for row_number, row_data in enumerate(cocina):
            # Insertar datos en todas las columnas, incluida la primera columna
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                tabla.setItem(row_number, column_number, item)

            # Hacer la primera columna invisible
            tabla.setColumnHidden(0, True)

            # Crear botones de editar y eliminar
            buttonEditar = QPushButton("Editar")
            buttonEditar.clicked.connect(lambda _, row=row_number: self.subirNivel(tabla, row, row_data[
                0]))  # Pasar el id de la fila como argumento
            buttonEditar.setStyleSheet("background-color: rgba(229,170,39,255);"
                                       " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            tabla.setCellWidget(row_number, 3, buttonEditar)  # Ajustar el índice para el botón editar

            buttonEliminar = QPushButton("Eliminar")
            buttonEliminar.clicked.connect(lambda _, row=row_number: self.delete_row(row, tabla, row_data[
                0]))  # Pasar el id de la fila como argumento
            buttonEliminar.setStyleSheet("background-color: rgba(247,67,56,255);"
                                         " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            tabla.setCellWidget(row_number, 4, buttonEliminar)

    def subirNivel(self, tabla, row, id_nivel):

        nivel = tabla.item(row, 0).text()
        nombre = tabla.item(row, 1).text()

        self.modeloNivel.updateNivel(nivel, nombre, id_nivel)

        self.listarNivel(tabla)



    def delete_row(self, row, tabla, id_categoria):
        # Preguntar al usuario si está seguro de eliminar la fila
        respuesta = QMessageBox.question(None, "Confirmación", "¿Estás seguro de eliminar este Nivel?",
                                         QMessageBox.Yes | QMessageBox.No)

        if respuesta == QMessageBox.Yes:
            # Si el usuario confirma que está seguro
            # Verificar si hay habitaciones asociadas a esta categoría
            habitaciones_asociadas = self.modeloNivel.obtenerHabitacionesPorNivel(id_categoria)

            if not habitaciones_asociadas:
                # Si no hay habitaciones asociadas, eliminar la categoría
                self.modeloNivel.eliminarNivel(id_categoria)

                # Si se elimina con éxito de la base de datos, eliminar la fila de la tabla
                tabla.removeRow(row)
                self.listarNivel(tabla)
            else:
                # Si hay habitaciones asociadas, mostrar un mensaje de error y no permitir la eliminación
                QMessageBox.critical(None, "Error",
                                     "No se puede eliminar este nivel porque hay habitaciones asociadas.")
        else:
            # Si el usuario cancela la acción, no hacer nada
            return

    # *** Este metodo es para optener cuantos niveles hay esto para la seccion de chekout *****
    def updateNivel(self, tabla):
        # ids = self.modeloNivel.actualizar_datos_automaticamente()
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
                self.modeloNivel.updatepisonivel(prod[2], prod[1], prod[0])

        self.listarNivel(tabla)

    def numeroNivel(self):
        numeroH = self.modeloNivel.obtener_idPisoHabitacionpornivel()
        return numeroH

    def CrearNivel(self, Nombre, Numero):
        if not Nombre or not Numero:
            print("Datos vacios")
        else:
            self.modeloNivel.insertarNivel(Nombre, Numero)
