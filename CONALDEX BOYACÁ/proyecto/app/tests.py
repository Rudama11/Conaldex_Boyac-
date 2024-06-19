from django.test import TestCase

from  pathlib import Path
import sys 

sys.path.append(str(Path(__file__).parent.parent))
from proyecto.wsgi import*
from app.models import Categoria,Ubicacion,Empleado

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