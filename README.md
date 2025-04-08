# # Gestion-de-Inventario-para-Pequeñas-Empresas

Un emprendedor nos ha solicitado una aplicación sencilla para gestionar su inventario de productos en la bodega de su negocio. Nos ha dicho que, con tanta tecnología, necesita algo práctico y funcional.


## 1. Requerimientos (Validación)

- CRUD de Productos: El sistema debe permitir al usuario realizar operaciones de creación, lectura, actualización y eliminación (CRUD) de productos en el inventario. Cada producto debe contener los siguientes atributos:
  
a. Nombre: Cadena de texto obligatoria que corresponde al nombre del producto

b. Descripción: Cadena de texto obligatoria que corresponde a las características del producto

c. Cantidad disponible: Numero entero mayor o igual a 0 que corresponde a las existencias del producto

d. Precio: Número entero mayor o igual a 0 correspondiente al precio unitario del producto

e. Categoría: Cadena de texto obligatoria que es ingresado manualmente por el usuario, la cual sirve para clasificar a los productos
Para validar esto el CRUD debe no permitir nombres de productos vacíos, la             cantidad disponible y precio unitarios no deben ser valores negativos y el usuario deberá ingresar manualmente las categorías de cada producto.
- Gestión de Stock: El sistema debe permitir actualizar la cantidad de productos cuando:
  
a. Se realice una venta, reduciendo la cantidad disponible

b. Se reciban nuevas unidades, incrementando la cantidad disponible
Para validar esto el sistema no podrá permitir que se vendan mas unidades de un producto de las disponibles en el inventario y no se permitirá registrar una cantidad negativa al recibir productos.
- Filtrado y Búsqueda: El sistema debe permitir a los usuarios buscar y filtrar productos de la siguiente manera:
  
a. Búsqueda por nombre: El usuario podrá ingresar un texto y el sistema mostrará productos cuyos nombres coincidan parcial o totalmente con la búsqueda solicitada

b. Filtrado por categoría: El usuario podrá ingresar un texto y el sistema mostrará todos los productos cuyas categorías coincidan con lo solicitado por el usuario

c. Orden por precio: El usuario podrá ordenar los productos de manera decreciente o creciente.
Para validar esto el sistema deberá mostrar todas las posibles opciones que coincidan con lo que quiere el usuario, ya sea por el filtro por categorías o búsqueda por nombre
- Generación de Reportes: El sistema debe permitir la generación de reportes con la siguiente información:
  
a. Total de productos en inventario: Número total de productos registrados con sus respectivos precios unitarios y las cantidades disponibles

b. Productos agotados: Listado de productos con cantidad disponible igual a 0 

c. Valor total del inventario: Suma de todos los precios unitarios de cada producto disponible en inventario.

Los reportes se mostraran por la terminal utilizada y para validar esto las cantidades totales deberán mostrar correctamente 
- Autenticación de Usuario: El acceso al sistema debe estar protegido mediante un sistema de autenticación basado en nombre y contraseña. El usuario estará predefinido de antes y no se permitirá la creación de nuevos usuarios desde el sistema

## 2. Verificación

La verificación se realizará a través de:
- Revisión de requerimientos: Comparación del sistema desarrollado con los requerimientos definidos para garantizar que todas las funcionalidades solicitadas han sido implementadas correctamente.
- Revision de codigo: Evaluación del código para verificar la correcta implementación de funciones
- Pruebas unitarias: Ejecución de pruebas para validar el comportamiento individual de los modelos del sistema
- Pruebas de integración: Verificación d la correcta comunicación entre los diferentes módulos del sistema

## 3. Organización y flujo

Para el desarrollo del proyecto, el equipo estuvo conformado por dos personas que se organizaron desde el inicio a través de una reunión de planificación. En dicha reunión se acordó la división de tareas y se definieron los canales de comunicación y herramientas de trabajo.

El desarrollo se dividió de la siguiente manera: uno de los integrantes se encargó de programar la mayor parte de la aplicación, mientras que el otro completó las funcionalidades faltantes y se dedicó principalmente a corregir errores encontrados durante las pruebas. Esta división permitió avanzar de forma ordenada y eficiente, asegurando que ambas partes aportaran al cumplimiento de los objetivos del proyecto.

Nos comunicamos principalmente a través de WhatsApp, Discord y Slack, dependiendo de la disponibilidad y del tipo de coordinación requerida. Además, configuramos un repositorio en GitHub con integración a Slack, donde activamos la revisión de pull requests obligatoria por parte del otro integrante antes de hacer merge a la rama principal.

Cada integrante trabajó en su propia rama sin seguir una estrategia de ramas específica, ya que no se programó en paralelo, sino en distintos momentos. Aun así, esto evitó conflictos en el código y permitió mantener un control ordenado de los cambios realizados.

Se realizaron dos ciclos de pruebas unitarias con greentest.ai. En el primero se identificaron errores que fueron corregidos, y posteriormente se ejecutó un segundo ciclo donde se verificó que todo funcionara correctamente. Este proceso de verificación nos permitió asegurar la calidad del software antes de finalizar el desarrollo.

## 4. Evidencia

- Pull requests:
![evidencia1](https://github.com/user-attachments/assets/825e753f-fe5e-4742-9b28-4a3473450f1a)

- Configuración GitHub:
  
![image](https://github.com/user-attachments/assets/21967166-e6f0-4edb-9ca0-c5c3a1b393f0)

- Slack conectado a GitHub:
  
 ![image](https://github.com/user-attachments/assets/f8615db3-f95d-4986-8a46-f7d9da5f91f5)

- Pruebas (Greentest.ai):
  
![image](https://github.com/user-attachments/assets/72621b54-e274-4ed5-ab04-cb7d3a0bbd77)

- Sentri.io conectado a Slack:

![image](https://github.com/user-attachments/assets/e396ef40-d65d-48ca-b946-8768f36e315d)


## 5. Problemas encontrados

No se presentaron mayores inconvenientes durante el trabajo en equipo, lo que facilitó un desarrollo fluido y colaborativo.

## Experiencia de uso de Greentest.ai

La app es relativamente buena, es muy cómoda para realizar las pruebas unitarias, pero es muy poco intuitiva para alguien que está recién descubriendo la app. El uso de la IA para solicitar pruebas es muy bueno y de hecho lo utilizamos ya que era más cómodo. Crear manualmente una prueba es poco cómodo, no se entiende muy bien que hay que hacer si no hay alguna ayuda o algún tipo de indicador, por esto mismo solo usamos la IA para crear las pruebas. Además existe un pequeño error en cuanto se escribe la descripción, si se hace un copy paste para el cuadro de texto y hay algun caracter no aceptado por la app no se indica que tipo de carácter es el que está incorrecto solo manda el error de texto. Ademas estaria bueno agregar algun tipo de documentacion para poder orientarse mejor de las funcionalidades que se pueden hacer en la app.

## Como usar el programa

Para utilizar el sistema se debera tener instalado python en el dispositivo que se desea utilizar. No se requiera instalar librerias externas

## Contribuciones

Los Pull Request son bienvenidos. Para solicitar un cambio significativo abrir una incidencia para comentar que desea cambiar


## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
