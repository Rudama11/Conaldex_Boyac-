from django.db import models
from datetime import datetime
from datetime import date
# Create your models here.

class Empleado(models.Model):
    Cedula='CC'
    Cedula_Extranjeria='CE'
    Tipo_Documento_CHOICES=[(Cedula,'Cedula de ciudadania'),(Cedula_Extranjeria,'Cedula de extranjeria')]
    nombres = models.CharField(max_length = 100,verbose_name='Nombres')
    apellidos = models.CharField(max_length = 100,verbose_name='Apellidos')
    Tipo_Documento=models.CharField(max_length=2,choices=Tipo_Documento_CHOICES,default=Cedula)
    correo=models.EmailField(max_length=250, unique=True, default="example@example.com")
    fecha_nacimiento=models.DateField(default=datetime.now,verbose_name='Fecha nacimiento')
    telefono=models.IntegerField(default=True)

    def __str__(self):
        return self.nombres
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleado'
        #ordering = ['id']

#----------------------------------------------------------------

class Ubicacion(models.Model):
    id = models.CharField(primary_key=True,max_length=6)
    Departamento=models.CharField(max_length=100,verbose_name='Departamento')
    Ciudad=models.CharField(max_length=100,verbose_name='Ciudad')
    
    def __str__(self):
        return self.Ciudad
    
    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'
        db_table = 'Ubicacion'
       # ordering = ['id']
    
#----------------------------------------------------------------
class Cliente(models.Model):
    Cedula='CC'
    Cedula_Extranjeria='CE'
    Tarjeta_Identidad='TI'
    Tipo_Documento_CHOICES=[(Cedula,'Cedula de ciudadania'),(Cedula_Extranjeria,'Cedula de extranjeria'),(Tarjeta_Identidad,'Tarjeta de identidad')]
    Tipo_Documento=models.CharField(max_length=2,choices=Tipo_Documento_CHOICES,default=Cedula)
    nombres = models.CharField(max_length = 100,verbose_name='Nombres')
    apellidos = models.CharField(max_length = 100,verbose_name='Apellidos')
    correo=models.EmailField(max_length=250, unique=True, default="example@example.com")
    fecha_nacimiento=models.DateField(default=date.today, verbose_name='Fecha nacimiento')
    cod_postal=models.ForeignKey(Ubicacion,max_length=6,on_delete= models.CASCADE)
    direccion=models.CharField(max_length=150,null=True,blank=True,verbose_name='Direccion')
    telefono=models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombres
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
        #ordering = ['id']
    
#----------------------------------------------------------------
class Categoria(models.Model):
    nombre = models.CharField(max_length = 100,verbose_name='Nombre')
    Ciudad=models.CharField(max_length=100,verbose_name='Ciudad')
    
    def __str__(self):
        return self.nombre 
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural='Categorias'
        db_table='Categoria'
        #ordering=[id]
    
#----------------------------------------------------------------

class Proveedor(models.Model):
    Cedula='CC'
    Cedula_Extranjeria='CE'
    Tipo_Documento_CHOICES=[(Cedula,'Cedula de ciudadania'),(Cedula_Extranjeria,'Cedula de extranjeria')]
    nombres = models.CharField(max_length = 100,verbose_name='Nombres')
    apellidos = models.CharField(max_length = 100,verbose_name='Apellidos')
    correo=models.EmailField()
    telefono=models.IntegerField(default=0)
    cod_postal=models.ForeignKey(Ubicacion,on_delete= models.CASCADE,max_length=6,)
    direccion=models.CharField(max_length=150,null=True,blank=True,verbose_name='Direccion')
    Tipo_Documento=models.CharField(max_length=2,choices=Tipo_Documento_CHOICES,default=Cedula)
    
    def __str__(self):
        return self.nombres
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedor'
       # ordering = ['id']
#----------------------------------------------------------------

class Producto(models.Model):
    Descripcion = models.CharField(max_length=300, verbose_name='Descripcion')
    Stock = models.IntegerField(default=True)
    Precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=3)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    
    def __str__(self):
        return self.Descripcion
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
       # ordering = ['id']

#----------------------------------------------------------------
class Compra(models.Model):
    cantidad_producto=models.IntegerField(default=0)
    precio_unitario=models.DecimalField(default=0.00,max_digits=9,decimal_places=3)
    precio_total=models.DecimalField(default=0.00,max_digits=9,decimal_places=3)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE,default=True)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,default=True)
    def __str__(self):
        return format(self.id)
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'Compra'
      #  ordering = ['id']
#----------------------------------------------------------------

class Normativa(models.Model):
    decreto=models.CharField(max_length=150,verbose_name='Decreto')
    detalles=models.CharField(max_length=500,verbose_name='Detalles')
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,default=True)
    
    def __str__(self):
        return self.decreto
    class Meta:
        verbose_name = 'Normativa'
        verbose_name_plural = 'Normativas'
        db_table = 'Normativa'
      #  ordering = ['id']
#----------------------------------------------------------------
class Venta(models.Model):
    cantidad=models.IntegerField(default=True)
    iva=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    precio_unitario=models.DecimalField(default=0.00, max_digits=9, decimal_places=3)
    precio_total=models.DecimalField(default=0.00, max_digits=9, decimal_places=3)
    descuento=models.DecimalField(default=0.00,max_digits=9,decimal_places=2)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,default=True)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,default=True)
    def __str__(self):
        return format(self.id)
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'
      #  ordering = ['id']
      
#----------------------------------------------------------------

class Registro_venta(models.Model):
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE,default=True)
    venta=models.ForeignKey(Venta,on_delete=models.CASCADE,default=True)
    def __str__(self):
        return format(self.id)
    class Meta:
        verbose_name = 'Registro_venta'
        verbose_name_plural = 'Registro_ventas'
        db_table = 'Registro Venta'
      #  ordering = ['id']

#----------------------------------------------------------------