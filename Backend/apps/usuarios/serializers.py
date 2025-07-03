from rest_framework import serializers
from .models import *


class usuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = usuarios
        fields = ('__all__')