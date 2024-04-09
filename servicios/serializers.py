# serializers.py
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # fields = ['email', 'contrasena', 'detalle_usuario']
        fields = "__all__"
