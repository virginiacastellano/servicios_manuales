from django.http import JsonResponse
from .models import Usuario, Resena, DetalleUsuario, Servicio, Prestador, MetodoPago, Categoria, SubCategoria, Cliente, Publicacion
# servicios/views.py
from rest_framework import generics
from .serializers import UsuarioSerializer

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# Vista para obtener todos los usuarios
def obtener_usuarios(request):
    usuarios = Usuario.objects.all()
    data = [{'email': usuario.email, 'nombre': usuario.detalle_usuario.nombre} for usuario in usuarios]
    return JsonResponse(data, safe=False)

# Vista para obtener todas las reseñas
def obtener_resenas(request):
    resenas = Resena.objects.all()
    data = [{'titulo': resena.titulo, 'comentario': resena.comentario, 'valoracion': resena.valoracion} for resena in resenas]
    return JsonResponse(data, safe=False)

# Vista para obtener todos los detalles de usuarios
def obtener_detalles_usuarios(request):
    detalles_usuarios = DetalleUsuario.objects.all()
    data = [{'nombre': detalle_usuario.nombre, 'apellido': detalle_usuario.apellido, 'edad': detalle_usuario.edad} for detalle_usuario in detalles_usuarios]
    return JsonResponse(data, safe=False)

# Vista para obtener todos los servicios
def obtener_servicios(request):
    servicios = Servicio.objects.all()
    data = [{'nombre': servicio.nombre, 'descripcion': servicio.descripcion} for servicio in servicios]
    return JsonResponse(data, safe=False)

# Vista para obtener todos los prestadores
def obtener_prestadores(request):
    prestadores = Prestador.objects.all()
    data = [{'id': prestador.id, 'servicio': prestador.servicio.nombre, 'usuario': prestador.detalle_usuario.nombre} for prestador in prestadores]
    return JsonResponse(data, safe=False)

# Vista para obtener todos los métodos de pago
def obtener_metodos_pago(request):
    metodos_pago = MetodoPago.objects.all()
    data = [{'nombre': metodo_pago.nombre} for metodo_pago in metodos_pago]
    return JsonResponse(data, safe=False)

# Vista para obtener todas las categorías
def obtener_categorias(request):
    categorias = Categoria.objects.all()
    data = [{'nombre': categoria.nombre} for categoria in categorias]
    return JsonResponse(data, safe=False)

# Vista para obtener todas las subcategorías
def obtener_subcategorias(request):
    subcategorias = SubCategoria.objects.all()
    data = [{'nombre': subcategoria.nombre} for subcategoria in subcategorias]
    return JsonResponse(data, safe=False)

# Vista para obtener todos los clientes
def obtener_clientes(request):
    clientes = Cliente.objects.all()
    data = [{'id': cliente.id, 'usuario': cliente.detalle_usuario.nombre} for cliente in clientes]
    return JsonResponse(data, safe=False)

# Vista para obtener todas las publicaciones
def obtener_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    data = [{'descripcion': publicacion.descripcion, 'metodo_pago': publicacion.metodo_pago.nombre} for publicacion in publicaciones]
    return JsonResponse(data, safe=False)
