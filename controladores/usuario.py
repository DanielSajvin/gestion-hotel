from bd.conexion import conecciones

class Usuario():
    def __init__(self) -> None:
        self.conn = conecciones()  # Llama a la función para obtener la conexión
              
    def obtener_id(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(Id) FROM usuarios")

        count = cursor.fetchone()[0]
        if count is None:
            count = 1
        else:
            count += 1
        return count

    def obtener_usuairo(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT Id, Nombre, TipoUsuario_idTipoUsuario FROM usuarios """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def InsertarUsuario(self, nombre, usuario, contrasenia, TipoUsuario):
        id = self.obtener_id()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO usuarios (`Id`, `Nombre`, `Usuario`, `Contrasenia`, `TipoUsuario_idTipoUsuario`) VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, nombre, usuario, contrasenia, TipoUsuario))
            self.conn.commit()
            
    def ActualizarUsuario(self, Id, nombre, TipoUsuario):
        with self.conn.cursor() as cursor:
            sql = """UPDATE usuarios SET Nombre = %s,
            TipoUsuario_idTipoUsuario = %s WHERE Id = %s"""
            cursor.execute(sql, (nombre, TipoUsuario, Id))
            self.conn.commit()
            
    def obtenerUsuarioCod(self, cod):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE Id = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result
  
    def eliminarUsuario(self, id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM usuarios WHERE Id = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()