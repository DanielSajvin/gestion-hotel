from bd.conexion import conecciones

class Cocina():
    def __init__(self) -> None:
        self.conn = conecciones()  # Llama a la función para obtener la conexión
              
    def obtener_id(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idCocina) FROM cocina")

        count = cursor.fetchone()[0]
        if count is None:
            count = 1
        else:
            count += 1
        return count

    def obtener_alimento(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM cocina"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarAlimento(self, nombre, fechaIngreso, fechaExpiracion):
        id = self.obtener_id()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO cocina (`idCocina`, `Nombre`, `FechaIngreso`, `FechaExpiracion`) VALUES (%s,%s,%s,%s)"""
            cursor.execute(sql, (id, nombre, fechaIngreso, fechaExpiracion))
            self.conn.commit()
            
    def ActualizarAlimento(self, Id, nombre, entrada, vencimiento):
        with self.conn.cursor() as cursor:
            sql = """UPDATE cocina SET Nombre = %s, FechaIngreso = %s,
            FechaExpiracion = %s WHERE idCocina = %s"""
            cursor.execute(sql, (nombre, entrada, vencimiento, Id))
            self.conn.commit()
            
    def obtenerAlimentoCod(self, cod):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM cocina WHERE idCocina = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result
  
    def eliminarAlimento(self, id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM cocina WHERE idCocina = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()