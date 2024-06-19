from django.test import TestCase

from  pathlib import Path
import sys 

sys.path.append(str(Path(__file__).parent.parent))
from proyecto.wsgi import*
from app.models import Categoria,Ubicacion

# Create your tests here.
# from app.models import Categoria

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
#--------------------------------------------------------------------------------------------------------------------------------
#Ubicacion 
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
#Obtener el objeto Ubicacion con ID=1
u = Ubicacion.objects.get(id=1)
# Imprimir los atributos válidos del objeto Ubicacion
print(u.Departamento)
print(u.Ciudad)
# Editar los atributos del objeto Ubicacion
u.Departamento = 'Boyacá'
u.Ciudad = 'Duitama'
# Guardar los cambios en la base de datos
u.save()
# Recuperar el objeto actualizado de la base de datos para reflejar los cambios
u_actualizado = Ubicacion.objects.get(id=1)
# Imprimir los atributos actualizados del objeto Ubicacion
print(u_actualizado.Departamento)
print(u_actualizado.Ciudad)

#Eliminar 
# Categoria.objects.get (id=4).delete()
# print(consulta)


