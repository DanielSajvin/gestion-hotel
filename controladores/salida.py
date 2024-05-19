from bd.conexion import conecciones

class Registro:
    def __init__(self):
        self.conn = conecciones()


    def obteneriddetalleFactura(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idDetalle) FROM detallefactura")

        count = cursor.fetchone()[0]
        if count:
            count = count + 1
            return count
        else:
            count = 1
            return count

    def obtenerdatosFacturas(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT f.id, u.Id, h.id, f.Fecha, u.Nombre, h.Nombre FROM factura f 
	inner join usuarios u on f.Usuarios_Id = u.Id
    inner join huesped h on f.huesped_id = h.id""")
        habitacion_data = cursor.fetchall()
        return habitacion_data

    def obtenerdatosporHabitacion(self, habitacion):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT h.NoHabitacion, c.Nombre, h.Detalle, e.Estado, c.Precio,
                        u.Nombre, u.DPI, u.RazonVisita,
                        d.fechaEntrada
                        FROM habitaciones h 
                        INNER JOIN categoriahabitacion c ON h.CategoriaHabitacion_idCategoriaHabitacion = c.idCategoriaHabitacion
                        INNER JOIN nivelhabitacion n ON h.NivelHabitacion_idNivelHabitacion = n.idNivelHabitacion 
                        INNER JOIN estadohabitacion e ON h.EstadoHabitacion_id1 = e.id 
                        LEFT JOIN huesped u ON h.id = u.habitaciones_id
                        LEFT JOIN detallefactura d ON h.id = d.habitaciones_id
                        WHERE h.NoHabitacion = %s""", (habitacion,))
        habitacion_data = cursor.fetchall()
        return habitacion_data

    def obteneridporHabitacion(self, habitacion):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT id FROM habitaciones where NoHabitacion =  %s""", (habitacion,))
        habitacion_data = cursor.fetchall()
        return habitacion_data

    def obtenerCostoAlojamiento(self, habitacionId, fechaE):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT SubTotal, anticipo, Total FROM detallefactura 
        where habitaciones_id = %s  and fechaEntrada = %s""", (habitacionId, fechaE,))
        habitacion_data = cursor.fetchall()
        return habitacion_data


    def insertarFechaEntrada(self, idHabitacion, FechaE, subtotal, descuento, anticipo, total):
        id = self.obteneriddetalleFactura()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO detallefactura (idDetalle, fechaEntrada, SubTotal, descuento, anticipo,  Total, habitaciones_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (id, FechaE, subtotal, descuento, anticipo, total, idHabitacion))
            self.conn.commit()


    def insertarFechaEntrada(self,fechaS, FechaE, subtotal, descuento, anticipo, total, idExtras, idHabitacion, idFactura):
        id = self.obteneriddetalleFactura()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO detallefactura (idDetalle, fechaSalida, fechaEntrada, SubTotal, descuento,
             anticipo, Total, extras_idExtras, habitaciones_id, factura_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (id, fechaS, FechaE, subtotal, descuento, anticipo, total, idExtras, idHabitacion, idFactura))
            self.conn.commit()

    def obteneridFactura(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id) FROM factura")

        count = cursor.fetchone()[0]
        if count:
            count = count + 1
            return count
        else:
            count = 1
            return count

    def crearFactura(self, fecha, usuario_id, huesped_id):
        id = self.obteneridFactura()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO factura (id, Fecha, Usuarios_Id, huesped_id) 
            VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (id, fecha, usuario_id, huesped_id))
            self.conn.commit()

    def obtenerUltimoIdFactura(self):
        with self.conn.cursor() as cursor:
            sql = "SELECT MAX(id) FROM factura"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]

    def obtenerUltimoIdDetalleFactura(self):
        with self.conn.cursor() as cursor:
            sql = "SELECT MAX(idDetalle) FROM detallefactura"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]

    def updateFacturaRegistro(self, fecha, usuario_id, huesped_id, idFactura):
        with self.conn.cursor() as cursor:
            sql = """UPDATE factura SET Fecha = %s, Usuarios_Id = %s, huesped_id=%s WHERE id = %s"""
            cursor.execute(sql, (fecha, usuario_id, huesped_id, idFactura))
            self.conn.commit()

    def updateDetalleFactura(self, fechaS, extrasId, facturaId, idDetalle):
        with self.conn.cursor() as cursor:
            sql = """UPDATE detallefactura SET fechaSalida = %s, extras_idExtras = %s, factura_id=%s WHERE idDetalle = %s"""
            cursor.execute(sql, (fechaS, extrasId, facturaId, idDetalle))
            self.conn.commit()


