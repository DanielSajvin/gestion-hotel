from bd.conexion import conecciones

class RegistrarNivel:
    def __init__(self):
        self.conn = conecciones()

    def obteneridNivel(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idNivelHabitacion) FROM nivelhabitacion")

        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def obtenerNivel(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT idNivelHabitacion, Nivel, Nombre FROM nivelhabitacion"""

            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def obteneridPorNombre(self, nombre_nivel):
        with self.conn.cursor() as cursor:
            sql = "SELECT idNivelHabitacion FROM nivelhabitacion WHERE Nombre = %s"
            cursor.execute(sql, (nombre_nivel,))
            result = cursor.fetchone()
            if result:
                id_nivel = result[0]
                return id_nivel
            else:
                return None  # Devolver None si no se encontró el nivel de habitación con el nombre dado

    def obtenerNombreNivel(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT idNivelHabitacion, Nombre FROM nivelhabitacion"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def obtenerNombreCategoria(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT idCategoriaHabitacion, Nombre, Precio FROM categoriahabitacion"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def obtenerHabitacionesPorNivel(self, id_nivel):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM habitaciones WHERE NivelHabitacion_idNivelHabitacion = %s", (id_nivel,))
        habitaciones = cursor.fetchall()
        return habitaciones

    def insertarNivel(self, nombre, nivel):
        id = self.obteneridNivel()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO nivelhabitacion (idNivelHabitacion, Nombre, Nivel) VALUES (%s, %s,%s)"""
            cursor.execute(sql, (id, nombre, nivel))
            self.conn.commit()

    def obtener_idPisoHabitacion(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idNivelHabitacion) FROM nivelhabitacion")

        count = cursor.fetchone()[0]
        if count is None:
            count = 1
        else:
            count += 1
        return count

    def obtener_idPisoHabitacionpornivel(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM nivelhabitacion")

        count = cursor.fetchone()[0]
        return count

    def updatepisonivel(self, nombre, nivel, id):
        with self.conn.cursor() as cursor:
            sql = """UPDATE nivelhabitacion SET Nombre = %s, Nivel = %s WHERE idNivelHabitacion = %s"""
            cursor.execute(sql, (nombre, nivel, id))
            self.conn.commit()

    def eliminarNivel(self, id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM nivelhabitacion WHERE idNivelHabitacion = '" + str(id) + "'"
            cursor.execute(sql)
            self.conn.commit()

    def updateNivel(self, nivel, nombre, id):
        with self.conn.cursor() as cursor:
            sql = """UPDATE nivelhabitacion SET Nombre = %s, Nivel = %s
                     WHERE idNivelHabitacion = %s """

            cursor.execute(sql, (nombre, nivel, id))
            self.conn.commit()

    def todoslosid_nivel(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT idNivelHabitacion FROM nivelhabitacion")
        result = cursor.fetchall()
        # Extraer los identificadores de las tuplas y guardarlos en una lista
        ids = [row[0] for row in result]
        return ids

    def actualizar_datos_automaticamente(self):
        while True:
            # Actualizar los datos llamando a la función todoslosid_nivel()
            ids = self.todoslosid_nivel()
            return ids

