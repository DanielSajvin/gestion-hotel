from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.habitacion import Habitacion
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget

class ModeloHabitacion():
    def __init__(self) -> None:
        self.modeloHabitacion = Habitacion()

    def listarHabitacion(self, tabla):
        # Obtener datos de la base de datos
        habitacion = self.modeloHabitacion.obtenertablaHabitacion()

        # Establecer el número de filas en la tabla
        tabla.setRowCount(len(habitacion))

        # Insertar los datos en la tabla
        for row_number, row_data in enumerate(habitacion):
            # Insertar datos en todas las columnas, incluida la primera columna
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                tabla.setItem(row_number, column_number, item)

            # Hacer la primera columna invisible
            tabla.setColumnHidden(0, True)
            tabla.setColumnHidden(1, True)
            tabla.setColumnHidden(2, True)
            tabla.setColumnHidden(3, True)

            # Crear botones de editar y eliminar
            buttonEditar = QPushButton("Editar")
            # Pasar el id de la fila como argumento
            buttonEditar.clicked.connect(lambda _, row=row_number: self.edit_row(row))

            buttonEditar.setStyleSheet("background-color: rgba(229,170,39,255);"
                                       " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            tabla.setCellWidget(row_number, 9, buttonEditar)  # Ajustar el índice para el botón editar

            buttonEliminar = QPushButton("Eliminar")
            # Pasar el id de la fila como argumento usando una función auxiliar
            buttonEliminar.clicked.connect(self.make_delete_callback(tabla, row_number, row_data[0]))

            buttonEliminar.setStyleSheet("background-color: rgba(247,67,56,255);"
                                         " color: rgba(255,255,255,255); font: 75 12pt 'Archivo';")
            tabla.setCellWidget(row_number, 10, buttonEliminar)

    def make_delete_callback(self, tabla, row, id):
        return lambda: self.delete_row(row, tabla, id)

    def delete_row(self, row, tabla, id_habitacion):
        # Preguntar al usuario si está seguro de eliminar la fila
        respuesta = QMessageBox.question(None, "Confirmación", "¿Estás seguro de eliminar este Nivel?",
                                         QMessageBox.Yes | QMessageBox.No)

        if respuesta == QMessageBox.Yes:
            # Si el usuario confirma que está seguro
            # Verificar si hay habitaciones asociadas a esta categoría
            print(id_habitacion)
            habitaciones_asociadas = self.modeloHabitacion.verificarhabitacionendetalle(id_habitacion)

            if not habitaciones_asociadas:
                # Si no hay habitaciones asociadas, eliminar la categoría
                self.modeloHabitacion.eliminarHabitacion(id_habitacion)

                # Si se elimina con éxito de la base de datos, eliminar la fila de la tabla
                tabla.removeRow(row)
                self.listarHabitacion(tabla)
            else:
                # Si hay habitaciones asociadas, mostrar un mensaje de error y no permitir la eliminación
                QMessageBox.critical(None, "Error",
                                     "No se puede eliminar esta habitacion por que hay registros que se perderian.")
        else:
            # Si el usuario cancela la acción, no hacer nada
            return


    def edit_row(self, row):
        print(f"se edita el botn: {row}")


    def CrearHabitacion(self, Numero, Detalle, Categoria, Nivel, Estado):
        if Numero and Estado and Categoria and Detalle and Nivel:
            self.modeloHabitacion.insertarHabitacion(Numero, Detalle, Categoria, Nivel, Estado)

    def obtenerDatosHabitacionInterfaz(self):
        habitacion = self.modeloHabitacion.obtenerDatosHabitacionInterfaz()
        return habitacion

    def obtenerDatosHabitacionInterfazSalida(self):
        habitacion = self.modeloHabitacion.obtenerDatosHabitacionInterfazSalida()
        return habitacion

    def updatehabitacion(self, tabla):
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

        # print(products)

        if len(products) > 0:
            for prod in products:
                self.modeloHabitacion.updateHabitacion(prod[0], prod[4], prod[7], prod[1], prod[2], prod[3])

                # Id, Numero, Detalle, Categoria, Nivel, Estado)

        self.listarHabitacion(tabla)

    def updateEstadoHabitacion(self, estado, idHabitacion, tabla):
        # Iterar sobre las filas de la tabla para encontrar la habitación con el id especificado
        for fila in range(tabla.rowCount()):
            if tabla.item(fila, 0).text() == str(idHabitacion):  # Comprobar si el id coincide
                # Actualizar el estado de la habitación
                tabla.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(estado)))
                # Salir del bucle una vez que se ha actualizado la habitación
                break
        else:
            # Si el bucle no se rompe, significa que no se encontró ninguna habitación con el id especificado
            print("No se encontró ninguna habitación con el id especificado:", idHabitacion)

        # self.modeloHabitacion.ActualizarEstadoHabitacion(estado, idHabitacion)
        self.updatehabitacion(tabla)
