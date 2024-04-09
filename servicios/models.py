from django.db import models




class Usuario(models.Model):
    
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    detalle_usuario = models.OneToOneField('DetalleUsuario', on_delete=models.CASCADE)

class DetalleUsuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    latitud = models.CharField(max_length=255)
    longitud = models.CharField(max_length=255)

class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

class Prestador(models.Model):
    servicio_ofrecido = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    detalle_usuario = models.OneToOneField(DetalleUsuario, on_delete=models.CASCADE)

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=255)

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

class SubCategoria(models.Model):
    nombre = models.CharField(max_length=255)
    servicios_usuario = models.ForeignKey(Servicio, on_delete=models.CASCADE)

class Cliente(models.Model):
    detalle_usuario = models.OneToOneField(DetalleUsuario, on_delete=models.CASCADE)

class Publicacion(models.Model):
    descripcion = models.CharField(max_length=255)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

class Resena(models.Model):
    titulo = models.CharField(max_length=255)
    comentario = models.TextField()
    valoracion = models.IntegerField()
    fecha = models.DateField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    publicacion_relacionada = models.ForeignKey('Publicacion', on_delete=models.CASCADE)
