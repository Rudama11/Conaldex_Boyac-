from django.test import TestCase

from  pathlib import Path
import sys 

sys.path.append(str(Path(__file__).parent.parent))
from proyecto.wsgi import*
from app.models import Categoria,Ubicacion,Empleado,Producto

# Create your tests here.
#---------------------------------------------------------------- CLASE EMPLEADO --------------------------------------------
# Empleado.objects.all().delete()
# Consulta = Empleado.objects.all()
# print (Consulta)
# #Insertar empleados a la clase empleado
# em=Empleado(Tipo_Documento= "CE",nombres="Juan Carlos",apellidos="Cardenas Perez",correo="carlosperez01@gmail.com",fecha_nacimiento="2000-07-13",telefono=3123461522).save()
# Consulta=Empleado.objects.all()
# print (Consulta)
# em=Empleado(Tipo_Documento= "CC",nombres="Laura Camila",apellidos="Rojas Gonzalez",correo="camigonzalez@gmail.com",fecha_nacimiento="2001-09-04",telefono=3224127846).save()
# Consulta=Empleado.objects.all()
# print (Consulta)
# em=Empleado(Tipo_Documento= "CC",nombres="Carlos",apellidos="Rodriguez",correo="carlosrod123@gmail.com",fecha_nacimiento="1999-11-14",telefono=3138451247).save()
# Consulta=Empleado.objects.all()
# print (Consulta)

# #Editar nombre empleado cuyo id es 2
# em=Empleado.objects.get(id=2)
# em.nombres="Juan"
# em.save()
# Consulta=Empleado.objects.all()
# print (Consulta)

# #Eliminar empleado id 3
# em=Empleado.objects.get(id=3)
# em.delete()
# Consulta=Empleado.objects.all()
# print(Consulta)
#---------------------------------------------------------------- CLASE CATEGORIA --------------------------------------------

# Categoria.objects.all().delete()

# Consulta todas las ubicaciones
# consulta_ubicaciones = Ubicacion.objects.all()
# print(list(consulta_ubicaciones))

# Insertar Categorías
# Categoria(nombre='Cascos', Ciudad="Sogamoso").save()
# Categoria(nombre='Extintor', Ciudad="Sogamoso").save()
# Categoria(nombre='Botas de Seguridad', Ciudad="Sogamoso").save()
# Categoria(nombre='Uniforme', Ciudad="Sogamoso").save()

# # Consulta todas las categorías
# consulta_categorias = Categoria.objects.all()
# print(list(consulta_categorias))


# Editar
# # Obtener el objeto Categoria con ID=1
# categoria = Categoria.objects.get(id=1)
# # Imprimir el nombre actual antes de la edición
# print(categoria.nombre)
# # Editar los atributos del objeto
# categoria.nombre = 'Extintor'
# categoria.ciudad = 'Sogamoso-Boyacá'
# # Guardar los cambios en la base de datos
# categoria.save()
# # Imprimir el nombre actualizado después de la edición
# print(categoria.nombre)

# Editar 
# Obtener el objeto Categoria con ID=1
# categoria = Categoria.objects.get(id=3)
# Imprimir el nombre actual antes de la edición
# print(categoria.nombre)
# Editar los atributos del objeto
# categoria.nombre = 'Botiquin'
# categoria.ciudad = 'Sogamoso-Boyacá'
# Guardar los cambios en la base de datos
# categoria.save()
# Imprimir el nombre actualizado después de la edición
# print(categoria.nombre)

#Eliminar 
# Categoria.objects.get (id=5).delete()
# consulta= Categoria.objects.all()
# print(consulta)

# obj =Categoria.objects.filter(nombre__contains = 'Cascos Proteccion',Ciudad__contains = 'Sogamoso Boyacá',).query
# print(obj)


# for i in Categoria.objects.filter():
#     print(i.nombre)
#---------------------------------------------------------------- CLASE UBICACION--------------------------------------------

#Insertar
# u= Ubicacion(id =1, Departamento ='Boyacá',Ciudad="Sogamoso").save()
# u= Ubicacion(id =2,Departamento ='Boyacá',Ciudad="Sogamoso").save()
# u= Ubicacion(id =3,Departamento ='Casanare',Ciudad="Yopal").save()
# u= Ubicacion(id =4,Departamento ='Bogota',Ciudad="Bogota").save()
# consulta = Ubicacion.objects.all()
# print(consulta)

#Eliminar 
# i= Ubicacion.objects.get (id=1).delete()
# u= Ubicacion.objects.get (id=2).delete()
# u= Ubicacion.objects.get (id=3).delete()
# u= Ubicacion.objects.get (id=4).delete()
# obj =Ubicacion.objects.filter(Departamento__contains = 'Bogota',Ciudad__contains = 'Bogota',).query
# print(obj)

# Editar
# #Obtener el objeto Ubicacion con ID=1
# u = Ubicacion.objects.get(id=1)
# # Imprimir los atributos válidos del objeto Ubicacion
# print(u.Departamento)
# print(u.Ciudad)
# # Editar los atributos del objeto Ubicacion
# u.Departamento = 'Boyacá'
# u.Ciudad = 'Duitama'
# # Guardar los cambios en la base de datos
# u.save()
# # Recuperar el objeto actualizado de la base de datos para reflejar los cambios
# u_actualizado = Ubicacion.objects.get(id=1)
# # Imprimir los atributos actualizados del objeto Ubicacion
# print(u_actualizado.Departamento)
# print(u_actualizado.Ciudad)

#Eliminar 
# Categoria.objects.get (id=4).delete()
# print(consulta)

#---------------------------------------------------------------- CLASE CATEGORÍA--------------------------------------------
#Insertar
# d1 = ([(6,"Protección Auditiva","Sogamoso"),
#     (7,"Protección Ocular","Sogamoso"),
#     (8,"Protección de Manos","Sogamoso"),
#     (9,"Protección Respiratoria","Sogamoso")])

# for i in d1:
#     Categoria(id=i[0],nombre=i[1],Ciudad=i[2]).save()
#     print("Se guardo con éxito")

#---------------------------------------------------------------- CLASE EMPLEADO--------------------------------------------
#Editar

# try:
#     em = Empleado.objects.get(id=4)
#     print(em.nombres)
#     em.nombres = "Miguel Camilo"
#     em.save()
#     print(f"Se cambio el nombre {em.nombres} correctamente")
# except Exception as e:
#     print(e)

#-------------------------------------- Class proveedor ----------------------------------------

#-------------------------------------BORRAR DATOS --------------------------------

# Proveedor.objects.all().delete()

#-------------------------------- LISTAS-------------------------------

# Consulta = Proveedor.objects.all()
# print (Consulta)

#----------------------------------- AGREGAR-------------------------------------

# u= Proveedor(id =1, nombres ='miguel',apellidos="castro",correo="correo1@gmail.com",telefono="3224567006",direccion="CR 5 N4-B",Tipo_Documento="CE",cod_postal_id="1").save()
# u= Proveedor(id =2, nombres ='Esteban',apellidos="zuares",correo="correo2@gmail.com",telefono="3207569506",direccion="CR 4 N63_56",Tipo_Documento="CC",cod_postal_id="2").save()
# consulta = Proveedor.objects.all()
# print(consulta)

#------------------------------------- EDITAR --------------------------------------------

# #Editar nombre empleado cuyo id es 2
# p=Proveedor.objects.get(id=2)
# p.nombres="Daniel"
# p.save()
# Consulta=Proveedor.objects.all()
# print (Consulta)

# #------------------------------------AGREGAR--------------------------------------

# Producto(Descripcion='Extintor 1', Stock=10, Categoria=Categoria.objects.first(), Precio=150.500).save()
# Producto(Descripcion='Extintor 2', Stock=20, Categoria=Categoria.objects.first(), Precio=200.750).save()

# #----------------------------------AGREGAR + PRODUCTO--------------------------------
# productos_nuevos = [
# {'Descripcion': 'Botas de Seguridad', 'Stock': 15, 'Precio': 120.000, 'Categoria': Categoria.objects.first()},
# {'Descripcion': 'Chaleco Reflectivo', 'Stock': 2, 'Precio': 80.500, 'Categoria': Categoria.objects.first()},
# {'Descripcion': 'Casco de Seguridad', 'Stock': 8, 'Precio': 50.000, 'Categoria': Categoria.objects.first()},

# ]
# for producto_data in productos_nuevos:
#     Producto(**producto_data).save()

# #--------------------------------CONSULTAR PRODUCTOS--------------------------------
# productos = Producto.objects.all()
# print("Lista de Productos:")
# for producto in productos:
#     print(f"- {producto.Descripcion} (Stock: {producto.Stock}, Precio: ${producto.Precio})")

# #------------------------EDITAR------------------------------------
# producto = Producto.objects.get(id=1)
# producto.Descripcion = 'Extintor ABC'
# producto.save()
# print(f"Producto '{producto.Descripcion}' editado correctamente.")

# #------------------------ELIMINAR---------------------------------------
# try:
#     producto = Producto.objects.get(id=2)
#     producto.delete()
#     print(f"Producto '{producto.Descripcion}' eliminado correctamente.")
# except Producto.DoesNotExist:
#     print("El producto con id=2 no existe.")

#------------------------------------AGREGAR Daniel--------------------------------------

# Producto(Descripcion='Extintor 1', Stock=10, Categoria=Categoria.objects.first(), Precio=150.500).save()
# Producto(Descripcion='Extintor 2', Stock=20, Categoria=Categoria.objects.first(), Precio=200.750).save()

#----------------------------------AGREGAR + PRODUCTO--------------------------------
# productos_nuevos = [
# {'Descripcion': 'Botas de Seguridad', 'Stock': 15, 'Precio': 120.000, 'Categoria': Categoria.objects.first()},
# {'Descripcion': 'Chaleco Reflectivo', 'Stock': 2, 'Precio': 80.500, 'Categoria': Categoria.objects.first()},
# {'Descripcion': 'Casco de Seguridad', 'Stock': 8, 'Precio': 50.000, 'Categoria': Categoria.objects.first()},
# ]
# for producto_data in productos_nuevos:
#     Producto(**producto_data).save()

#--------------------------------CONSULTAR PRODUCTOS--------------------------------
# productos = Producto.objects.all()
# print("Lista de Productos:")
# for producto in productos:
#     print(f"- {producto.Descripcion} (Stock: {producto.Stock}, Precio: ${producto.Precio})")

#------------------------EDITAR------------------------------------
# producto = Producto.objects.get(id=8)
# producto.Descripcion = 'Extintor 3'
# producto.save()
# print(f"Producto '{producto.Descripcion}' editado correctamente.")

#------------------------ELIMINAR---------------------------------------
from app.models import Producto
from django.core.exceptions import ObjectDoesNotExist

try: 
    productos = Producto.objects.filter(id__in=[12])
  
    for producto in productos:
        producto.delete()
        print(f"Producto '{producto.Descripcion}' eliminado correctamente.")

except ObjectDoesNotExist:
    print("El producto no existe.")