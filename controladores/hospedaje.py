from bd.conexion import conecciones

class RegistrarHospedaje:
    def __init__(self):
        self.conn = conecciones()

    def insertarHospedaje(self, nombre, dpi,razon, num):
        id = self.obteneridHuesped()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO huesped (id, Nombre, DPI, RazonVisita, habitaciones_id) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (id, nombre, dpi,  razon, num))
            self.conn.commit()

    def obtenerIdsHabitacionesOcupadas(self):
        cursor = self.conn.cursor()
        cursor.execute("""select c.id from huesped h inner join habitaciones c on h.habitaciones_id = c.id""")
        habitacion_data = cursor.fetchall()
        return habitacion_data


    def habitacionesenuso(self):
        cursor = self.conn.cursor()
        cursor.execute("""select c.id, c.NoHabitacion from huesped h inner join habitaciones c on h.habitaciones_id = c.id""")
        habitacion_data = cursor.fetchall()
        return habitacion_data

    def obteneridporHabitacion(self, habitacion):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT id FROM habitaciones where NoHabitacion =  %s""", (habitacion,))
        habitacion_data = cursor.fetchall()
        return habitacion_data

    def obtenerdatosporHabitacion(self, habitacion):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT h.NoHabitacion, c.Nombre, h.Detalle, e.Estado, c.Precio 
                        FROM habitaciones h 
                        INNER JOIN categoriahabitacion c ON h.CategoriaHabitacion_idCategoriaHabitacion = c.idCategoriaHabitacion
                        INNER JOIN nivelhabitacion n ON h.NivelHabitacion_idNivelHabitacion = n.idNivelHabitacion 
                        INNER JOIN estadohabitacion e ON h.EstadoHabitacion_id1 = e.id 
                        WHERE h.NoHabitacion = %s""", (habitacion,))
        habitacion_data = cursor.fetchall()
        return habitacion_data


    def obteneridHuesped(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id) FROM huesped")

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
