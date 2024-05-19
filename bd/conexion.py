import mysql.connector


def conecciones():
    try:
        # Establecer conexión con la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",
            db="hotel_ad",
            port=3306
        )
        return db
    except mysql.connector.Error as err:
        # Manejar errores de conexión
        print(f"Error al conectar a la base de datos: {err}")
        return None
