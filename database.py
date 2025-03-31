import sqlite3

def get_db_connection():
    conn = sqlite3.connect('inventario.db')
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    

    # Tabla de productos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL CHECK(cantidad >= 0),

        precio REAL NOT NULL,
        categoria TEXT
    )
    """)

    
    # Tabla de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    
    # Usuario predefinido (admin)
    cursor.execute("""
    INSERT OR IGNORE INTO usuarios (username, password) 
    VALUES ('admin', 'admin123')
    """)
    

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()

    print("✅ Base de datos inicializada correctamente.")

