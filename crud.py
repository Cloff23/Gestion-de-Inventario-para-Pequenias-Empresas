from database import get_db_connection



# Funcion para crear un producto

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


# Funcion para obtener todos los productos o filtrarlos
def obtener_productos(filtro=None, valor=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if filtro and valor:
        if filtro == "id":
            cursor.execute("SELECT * FROM productos WHERE id = ?", (valor,))
        elif filtro == "categoria":
            cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", (f'%{valor}%',))
        elif filtro == "nombre":
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f'%{valor}%',))
        elif filtro == "cantidad":
            cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (int(valor),))
    else:
        cursor.execute("SELECT * FROM productos")
        

    productos = cursor.fetchall()
    conn.close()
    return productos


# Funcion para obtener un producto por su ID
def actualizar_stock(id_producto, cantidad, operacion='aumentar'):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT cantidad FROM productos WHERE id = ?", (id_producto,))
    resultado = cursor.fetchone()
    
    if not resultado:
        conn.close()
        return False, "Producto no encontrado"
    
    cantidad_actual = resultado['cantidad']
    
    # Calcular nueva cantidad
    if operacion == 'aumentar':
        nueva_cantidad = cantidad_actual + cantidad
    else:
        nueva_cantidad = cantidad_actual - cantidad
    
    # Validar stock negativo
    if nueva_cantidad < 0:
        conn.close()
        return False, "No se puede tener stock negativo"
    
    # Actualizar
    cursor.execute(
        "UPDATE productos SET cantidad = ? WHERE id = ?",
        (nueva_cantidad, id_producto)
    )
    conn.commit()
    conn.close()

    return True, "Stock actualizado correctamente"

# Funcion para eliminar un producto

def eliminar_producto(id_producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
    conn.close()

# Funcion para autenticar un usuario
def autenticar_usuario(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    usuario = cursor.fetchone()
    conn.close()
    return usuario is not None

# Funcion para generar un reporte de los productos en el inventario
def generar_reporte():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Productos con stock
    cursor.execute("SELECT * FROM productos WHERE cantidad > 0")
    con_stock = cursor.fetchall()
    
    # Productos sin stock
    cursor.execute("SELECT * FROM productos WHERE cantidad = 0")
    sin_stock = cursor.fetchall()
    
    # Valor total del inventario
    cursor.execute("SELECT SUM(cantidad * precio) as total FROM productos WHERE cantidad > 0")
    total = cursor.fetchone()['total'] or 0
    
    conn.close()

    return con_stock, sin_stock, total

