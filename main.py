from models import Producto
from crud import *
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n SISTEMA DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Ver todos los productos")
    print("3. Actualizar stock")
    print("4. Eliminar producto")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            limpiar_pantalla()
            print("\n NUEVO PRODUCTO")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            categoria = input("Categoría: ")
            
            nuevo_producto = Producto(nombre, descripcion, cantidad, precio, categoria)
            crear_producto(nuevo_producto)
            print("\n✅ Producto creado correctamente!")
        
        elif opcion == "2":
            limpiar_pantalla()
            print("\n LISTA DE PRODUCTOS")
            productos = obtener_productos()
            for prod in productos:
                print(f"\nID: {prod['id']}")
                print(f"Nombre: {prod['nombre']}")
                print(f"Stock: {prod['cantidad']}")
                print(f"Precio: ${prod['precio']:.2f}")
                print(f"Categoría: {prod['categoria']}")
                print("-" * 30)
            input("\nPresione Enter para continuar...")
        
        elif opcion == "3":
            limpiar_pantalla()
            print("\n ACTUALIZAR STOCK")
            id_producto = int(input("ID del producto: "))
            nueva_cantidad = int(input("Nueva cantidad: "))
            actualizar_stock(id_producto, nueva_cantidad)
            print("\n✅ Stock actualizado!")
        
        elif opcion == "4":
            limpiar_pantalla()
            print("\n ELIMINAR PRODUCTO")
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)
            print("\n✅ Producto eliminado!")
        
        elif opcion == "5":
            print("\n👋 ¡Hasta pronto!")
            break
        
        else:
            print("\n Opción no válida")

if __name__ == '__main__':
    from database import init_db
    init_db()
    
    main()