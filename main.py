# main.py
from models import Producto
from crud import *
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    print("\n SISTEMA DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Ver todos los productos")
    print("3. Actualizar stock")
    print("4. Eliminar producto")
    print("5. Buscar productos")
    print("6. Generar reporte")
    print("7. Salir")

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
    
    nombre = input_con_salida("Nombre: ")
    if nombre is None: return
    
    descripcion = input_con_salida("Descripción: ")
    if descripcion is None: return
    
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
    
    categoria = input_con_salida("Categoría: ")
    if categoria is None: return
    
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
            menu_eliminar_producto()
        elif opcion == "5":
            menu_buscar_productos()
        elif opcion == "6":
            mostrar_reporte()
        elif opcion == "7":
            print("\n👋 ¡Hasta pronto!")
            break
        else:
            print("\n❌ Opción no válida")
            input("\nPresione Enter para continuar...")

if __name__ == '__main__':
    from database import init_db
    init_db()
    main()