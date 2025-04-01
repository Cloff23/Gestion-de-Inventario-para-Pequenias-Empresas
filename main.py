
# main.py
from models import Producto
from crud import *
import os

import sentry_sdk


sentry_sdk.init(
    dsn="https://8436fb52989d7719908d244eb7f4273f@o4509069881769984.ingest.us.sentry.io/4509069899005952",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu_principal():

    print("\n SISTEMA DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Ver todos los productos")
    print("3. Actualizar stock")
    print("4. Editar producto")  
    print("5. Eliminar producto")
    print("6. Buscar productos")
    print("7. Generar reporte")
    print("8. Salir")


def login():
    limpiar_pantalla()
    print("\n INICIO DE SESIÓN")
    intentos = 3
    
    while intentos > 0:
        username = input("Usuario: ")
        password = input("Contraseña: ")
        
        if autenticar_usuario(username, password):
            return True
        
        intentos -= 1
        print(f"\n❌ Credenciales incorrectas. Intentos restantes: {intentos}")
        input("Presione Enter para continuar...")
        limpiar_pantalla()
    
    print("\n⛔ Has agotado tus intentos. Saliendo del sistema...")
    return False

def mostrar_lista_productos():
    productos = obtener_productos()
    if not productos:
        print("\nNo hay productos registrados.")
        return False
    
    print("\n LISTA DE PRODUCTOS:")
    print("-" * 60)
    print("ID  | Nombre                | Stock | Precio   | Categoría")
    print("-" * 60)
    for prod in productos:
        print(f"{prod['id']:<3} | {prod['nombre'][:20]:<20} | {prod['cantidad']:<5} | ${prod['precio']:<7.2f} | {prod['categoria']}")
    print("-" * 60)
    return True

def input_con_salida(prompt):
    print("\n(Enter 'salir' para cancelar)")
    user_input = input(prompt)
    if user_input.lower() == 'salir':
        return None
    return user_input

def menu_agregar_producto():
    limpiar_pantalla()
    print("\n NUEVO PRODUCTO")
    
    while True:
        nombre = input_con_salida("Nombre: ")
        if nombre is None or nombre.strip() == "":
            print("❌ Por favor, escriba un nombre.")
            continue
        break
    
    while True:
        descripcion = input_con_salida("Descripción: ")
        if descripcion is None or descripcion.strip() == "":
            print("❌ Por favor, escriba una descripción.")
            continue
        break
    
    while True:
        cantidad = input_con_salida("Cantidad inicial: ")
        if cantidad is None: return
        try:
            cantidad = int(cantidad)
            if cantidad < 0:
                print("❌ La cantidad no puede ser negativa")
                continue
            break
        except ValueError:
            print("❌ Debe ingresar un número entero")
    
    while True:
        precio = input_con_salida("Precio: ")
        if precio is None: return
        try:
            precio = float(precio)
            if precio <= 0:
                print("❌ El precio debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("❌ Debe ingresar un número válido")
    
    while True:
        categoria = input_con_salida("Categoría: ")
        if categoria is None or categoria.strip() == "":
            print("❌ Por favor, escriba una categoría.")
            continue
        break
    
    nuevo_producto = Producto(nombre, descripcion, cantidad, precio, categoria)
    crear_producto(nuevo_producto)
    print("\nProducto creado correctamente!")
    input("\nPresione Enter para continuar...")

def menu_actualizar_stock():
    while True:
        limpiar_pantalla()
        print("\n ACTUALIZAR STOCK")
        
        if not mostrar_lista_productos():
            input("\nPresione Enter para volver...")
            return
        
        id_producto = input_con_salida("\nID del producto a actualizar: ")
        if id_producto is None: return
        
        try:
            id_producto = int(id_producto)
            producto = obtener_productos(filtro="id", valor=id_producto)
            if not producto:
                print("❌ No existe un producto con ese ID")
                input("Presione Enter para continuar...")
                continue
            producto = producto[0]
            break
        except ValueError:
            print("❌ Debe ingresar un número de ID válido")
            input("Presione Enter para continuar...")
    
    print(f"\nProducto seleccionado: {producto['nombre']} (Stock actual: {producto['cantidad']})")
    
    print("\n1. Aumentar stock")
    print("2. Disminuir stock")
    print("3. Cancelar")
    
    while True:
        opcion = input_con_salida("Seleccione operación: ")
        if opcion is None: return
        
        if opcion not in ["1", "2", "3"]:
            print("❌ Opción no válida")
            continue
        
        if opcion == "3":
            return
        
        operacion = 'aumentar' if opcion == "1" else 'disminuir'
        break
    
    while True:
        cantidad = input_con_salida(f"Cantidad a {operacion}: ")
        if cantidad is None: return
        
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("❌ Debe ingresar un número entero")
    
    exito, mensaje = actualizar_stock(id_producto, cantidad, operacion)
    print(f"\n{'✅' if exito else '❌'} {mensaje}")
    input("\nPresione Enter para continuar...")

def menu_eliminar_producto():
    while True:
        limpiar_pantalla()
        print("\n ELIMINAR PRODUCTO")
        
        if not mostrar_lista_productos():
            input("\nPresione Enter para volver...")
            return
        
        id_producto = input_con_salida("\nID del producto a eliminar: ")
        if id_producto is None: return
        
        try:
            id_producto = int(id_producto)
            producto = obtener_productos(filtro="id", valor=id_producto)
            if not producto:
                print("❌ No existe un producto con ese ID")
                input("Presione Enter para continuar...")
                continue
            
            producto = producto[0]
            print(f"\nProducto seleccionado: {producto['nombre']}")
            confirmar = input("¿Está seguro que desea eliminar este producto? (s/n): ").lower()
            if confirmar == 's':
                eliminar_producto(id_producto)
                print("\nProducto eliminado!")
            else:
                print("\nOperación cancelada")
            input("\nPresione Enter para continuar...")
            return
        except ValueError:
            print("Debe ingresar un número de ID válido")
            input("Presione Enter para continuar...")

def menu_buscar_productos():
    while True:
        limpiar_pantalla()
        print("\n BUSCAR PRODUCTOS")
        print("1. Por nombre")
        print("2. Por categoría")
        print("3. Por cantidad (menor o igual a)")
        print("4. Volver al menú principal")
        
        opcion = input_con_salida("\nSeleccione una opción: ")
        if opcion is None or opcion == "4":
            return
        
        if opcion == "1":
            nombre = input_con_salida("Ingrese nombre o parte del nombre: ")
            if nombre is None: continue
            productos = obtener_productos(filtro="nombre", valor=nombre)
        elif opcion == "2":
            categoria = input_con_salida("Ingrese categoría: ")
            if categoria is None: continue
            productos = obtener_productos(filtro="categoria", valor=categoria)
        elif opcion == "3":
            cantidad = input_con_salida("Ingrese cantidad máxima: ")
            if cantidad is None: continue
            try:
                cantidad = int(cantidad)
                productos = obtener_productos(filtro="cantidad", valor=cantidad)
            except ValueError:
                print("❌ Debe ingresar un número válido")
                input("Presione Enter para continuar...")
                continue
        else:
            print("❌ Opción no válida")
            input("Presione Enter para continuar...")
            continue
        
        mostrar_productos(productos)

def mostrar_productos(productos):
    limpiar_pantalla()
    if not productos:
        print("\nNo se encontraron productos.")
    else:
        print("\n RESULTADOS:")
        print("-" * 60)
        print("ID  | Nombre                | Stock | Precio   | Categoría")
        print("-" * 60)
        for prod in productos:
            print(f"{prod['id']:<3} | {prod['nombre'][:20]:<20} | {prod['cantidad']:<5} | ${prod['precio']:<7.2f} | {prod['categoria']}")
        print("-" * 60)
    input("\nPresione Enter para continuar...")

def mostrar_reporte():
    con_stock, sin_stock, total = generar_reporte()
    limpiar_pantalla()
    
    print("\nREPORTE DE INVENTARIO")
    
    print("\nPRODUCTOS CON STOCK:")
    if con_stock:
        for prod in con_stock:
            print(f"- {prod['nombre']} ({prod['cantidad']} unidades) - ${prod['precio']:.2f} c/u")
    else:
        print("No hay productos con stock")
    
    print("\nPRODUCTOS SIN STOCK:")
    if sin_stock:
        for prod in sin_stock:
            print(f"- {prod['nombre']} (agotado)")
    else:
        print("No hay productos sin stock")
    
    print(f"\nVALOR TOTAL DEL INVENTARIO: ${total:.2f}")
    input("\nPresione Enter para continuar...")

def menu_editar_producto():
    while True:
        limpiar_pantalla()
        print("\n EDITAR PRODUCTO")

        if not mostrar_lista_productos():
            input("\nPresione Enter para volver...")
            return

        id_producto = input_con_salida("\nID del producto a editar: ")
        if id_producto is None:
            return

        try:
            id_producto = int(id_producto)
            producto = obtener_productos(filtro="id", valor=id_producto)
            if not producto:
                print("❌ No existe un producto con ese ID")
                input("Presione Enter para continuar...")
                continue
            producto = dict(producto[0])  
            break
        except ValueError:
            print("❌ Debe ingresar un número válido")
            input("Presione Enter para continuar...")

    limpiar_pantalla()
    print("\n EDITANDO PRODUCTO")
    print(f"(Deje en blanco para mantener el valor actual)\n")

    nuevo_nombre = input_con_salida(f"Nombre [{producto['nombre']}]: ")
    if nuevo_nombre is not None and nuevo_nombre.strip() != "":
        producto['nombre'] = nuevo_nombre.strip()

    nueva_desc = input_con_salida(f"Descripción [{producto['descripcion']}]: ")
    if nueva_desc is not None and nueva_desc.strip() != "":
        producto['descripcion'] = nueva_desc.strip()

    while True:
        nueva_cantidad = input_con_salida(f"Cantidad [{producto['cantidad']}]: ")
        if nueva_cantidad is None or nueva_cantidad.strip() == "":
            break
        try:
            cantidad = int(nueva_cantidad)
            if cantidad < 0:
                print("❌ La cantidad no puede ser negativa")
                continue
            producto['cantidad'] = cantidad
            break
        except ValueError:
            print("❌ Debe ingresar un número entero")

    while True:
        nuevo_precio = input_con_salida(f"Precio [{producto['precio']}]: ")
        if nuevo_precio is None or nuevo_precio.strip() == "":
            break
        try:
            precio = float(nuevo_precio)
            if precio <= 0:
                print("❌ El precio debe ser mayor a 0")
                continue
            producto['precio'] = precio
            break
        except ValueError:
            print("❌ Debe ingresar un número válido")

    nueva_categoria = input_con_salida(f"Categoría [{producto['categoria']}]: ")
    if nueva_categoria is not None and nueva_categoria.strip() != "":
        producto['categoria'] = nueva_categoria.strip()

    # Guardar cambios
    actualizar_producto(producto)
    print("\n✅ Producto actualizado correctamente.")
    input("\nPresione Enter para continuar...")


def main():
    if not login():
        return
    
    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            menu_agregar_producto()
        elif opcion == "2":
            limpiar_pantalla()
            print("\n LISTA DE PRODUCTOS")
            mostrar_lista_productos()
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
            menu_actualizar_stock()
        elif opcion == "4":
            menu_editar_producto()  # <- nuevo
        elif opcion == "5":
            menu_eliminar_producto()
        elif opcion == "6":
            menu_buscar_productos()
        elif opcion == "7":
            mostrar_reporte()
        elif opcion == "8":
            print("\n👋 ¡Hasta pronto!")
            break
        else:
            print("\n❌ Opción no válida")
            input("\nPresione Enter para continuar...")


if __name__ == '__main__':
    from database import init_db
    init_db()
    main()