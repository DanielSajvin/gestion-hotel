from bd.conexion import conecciones

class RegistrarCategoria:
    def __init__(self):
        self.conn = conecciones()

    def obteneridCategoria(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idCategoriaHabitacion) FROM categoriahabitacion")

        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def obtenerCategoria(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM categoriahabitacion"""

            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    # ************* Este metodo sirve para optener en que habitaciones se esta usando alguna categoria*** ******
    def obtenerHabitacionesPorCategoria(self, id_categoria):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM habitaciones WHERE CategoriaHabitacion_idCategoriaHabitacion = %s", (id_categoria,))
        habitaciones = cursor.fetchall()
        return habitaciones

    def insertarCategoria(self, nombre, Precio):
        id = self.obteneridCategoria()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO categoriahabitacion (idCategoriaHabitacion, Nombre, Precio) VALUES (%s, %s,%s)"""
            cursor.execute(sql, (id, nombre, Precio))
            self.conn.commit()

    def eliminarCategoria(self, id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM categoriahabitacion WHERE idCategoriaHabitacion = '" + str(id) + "'"
            cursor.execute(sql)
            self.conn.commit()

    def updateCategoria(self, nombre, Precio, id):
        with self.conn.cursor() as cursor:
            sql = """UPDATE categoriahabitacion SET Nombre = %s, Precio = %s
                     WHERE idCategoriaHabitacion = %s """

            cursor.execute(sql, (nombre, Precio, id))
            self.conn.commit()

