from rest_framework import serializers
from .models import *

class rehberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kisi
        fields = ('Adi', 'Soyadi')
        #fields = ('__all__')