from django.contrib import admin
from django.urls import path
from servicios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', views.UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view(), name='usuario-detail'),
    path('resenas/', views.obtener_resenas, name='resena-list'),
    path('detalles-usuarios/', views.obtener_detalles_usuarios, name='detalle-usuario-list'),
    path('servicios/', views.obtener_servicios, name='servicio-list'),
    path('prestadores/', views.obtener_prestadores, name='prestador-list'),
    path('metodos-pago/', views.obtener_metodos_pago, name='metodo-pago-list'),
    path('categorias/', views.obtener_categorias, name='categoria-list'),
    path('subcategorias/', views.obtener_subcategorias, name='subcategoria-list'),
    path('clientes/', views.obtener_clientes, name='cliente-list'),
    path('publicaciones/', views.obtener_publicaciones, name='publicacion-list'),
]
