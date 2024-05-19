from bd.conexion import conecciones

class Huesped():
    def __init__(self) -> None:
        self.conn = conecciones()  # Llama a la función para obtener la conexión
              
    def obtener_id(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id) FROM huesped")

        count = cursor.fetchone()[0]
        if count is None:
            count = 1
        else:
            count += 1
        return count

    def obtenerHuesped(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM huesped"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarHuesped(self, nombre, dpi, anticipo, entrada, salida):
        id = self.obtener_id()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO huesped  (`id`, `Nombre`, `DPI`, `Anticipo`, `FechaEntrada`, `FechaSalida`)  VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, nombre, dpi, anticipo, entrada, salida))
            self.conn.commit()
            
    def ActualizarHuesped(self, Id, nombre, dpi, anticipo, entrada, salida):
        with self.conn.cursor() as cursor:
            sql = """UPDATE huesped SET Nombre = %s, DPI = %s, Anticipo = %s,
            FechaEntrada = %s, FechaSalida = %s WHERE id = %s"""
            cursor.execute(sql, (nombre, dpi, anticipo, entrada, salida, Id))
            self.conn.commit()
            
    def obtenerHuespedCod(self, cod):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM huesped WHERE id = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def obteneidhuespedporNombre(self, nombreHuesped):
        with self.conn.cursor() as cursor:
            sql = "SELECT id FROM huesped WHERE Nombre = %s"
            cursor.execute(sql, (nombreHuesped,))
            result = cursor.fetchone()
            if result:
                return result


    def eliminarHuesped(self, id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM huesped WHERE id = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()
