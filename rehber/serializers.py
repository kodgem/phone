from rest_framework import serializers
from .models import *

class kisiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kisi
        #fields = ('Adi', 'Soyadi')
        fields = ('__all__')


class kisiTelefonSerializer(serializers.ModelSerializer):

    class Meta:
        model = KisiTelefon
        fields = ('KisiTelefonID', 'Telefon', 'Tur', 'Kisi')
        #fields = ('__all__')


class rehberListSerializer(serializers.ModelSerializer):
    Kisi = kisiSerializer()
    KisiTelefon = kisiTelefonSerializer()
    class Meta:
        model = Kisi
        fields = ('Kisi', 'KisiTelefon')