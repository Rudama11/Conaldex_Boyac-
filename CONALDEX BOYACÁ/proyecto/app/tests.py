#from django.test import TestCase
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from proyecto.wsgi import *
from app.models import Ubicacion,Empleado
# Create your tests here.
# # Eliminar todos los registros de Empleado y Ubicacion
# Empleado.objects.all().delete()
# Ubicacion.objects.all().delete()
# Consulta = Empleado.objects.all()
# print (Consulta)
#Insertar
# em=Empleado(Tipo_Documento= "CE",nombres="Juan Carlos",apellidos="Cardenas Perez",correo="carlosperez01@gmail.com",fecha_nacimiento="2000-07-13",telefono=3123461522).save()
# Consulta=Empleado.objects.all()
# print (Consulta)
# em=Empleado(Tipo_Documento= "CC",nombres="Laura Camila",apellidos="Rojas Gonzalez",correo="camigonzalez@gmail.com",fecha_nacimiento="2001-09-04",telefono=3224127846).save()
# Consulta=Empleado.objects.all()
# print (Consulta)
# em=Empleado(Tipo_Documento= "CC",nombres="Carlos",apellidos="Rodriguez",correo="carlosrod123@gmail.com",fecha_nacimiento="1999-11-14",telefono=3138451247).save()
# Consulta=Empleado.objects.all()
# print (Consulta)

# #Editar
# em=Empleado.objects.get(id=2)
# em.nombres="Juan"
# em.save()
# Consulta=Empleado.objects.all()
# print (Consulta)

#Eliminar
# em=Empleado.objects.get(id=3)
# em.delete()
# Consulta=Empleado.objects.all()
# print(Consulta)


