from bd.conexion import conecciones

class TipoUsuario():
    def __init__(self) -> None:
        self.conn = conecciones()  # Llama a la función para obtener la conexión
              
    def obtener_id(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idTipoUsuario) FROM tipousuario")

        count = cursor.fetchone()[0]
        if count is None:
            count = 1
        else:
            count += 1
        return count

    def obtener_tipousuairo(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM tipousuario """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def InsertarTipoUsuario(self, TipoUsuario):
        id = self.obtener_id()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO tipousuario (`idTipoUsuario`, `TipoUsuariocol`) VALUES (%s,%s)"""
            cursor.execute(sql, (id, TipoUsuario))
            self.conn.commit()
            
    def ActualizarTipoUsuario(self, Id, TipoUsuario):
        with self.conn.cursor() as cursor:
            sql = """UPDATE tipousuario SET TipoUsuariocol = %s WHERE idTipoUsuario = %s"""
            cursor.execute(sql, (TipoUsuario, Id))
            self.conn.commit()
            
    def obtenerUsuarioCod(self, cod):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM tipousuario WHERE idTipoUsuario = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result
  
    def eliminarTipoUsuario(self, id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM tipousuario WHERE idTipoUsuario = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()