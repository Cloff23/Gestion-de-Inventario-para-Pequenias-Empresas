from database import get_db_connection

def crear_producto(producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        """,
        (producto.nombre, producto.descripcion, producto.cantidad, producto.precio, producto.categoria)
    )
    conn.commit()
    conn.close()

def obtener_productos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

def actualizar_stock(id_producto, nueva_cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE productos SET cantidad = ? WHERE id = ?",
        (nueva_cantidad, id_producto)
    )
    conn.commit()
    conn.close()

def eliminar_producto(id_producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
    conn.close()