import json
from django.shortcuts import render, HttpResponse
from .models import Kisi, KisiEposta, KisiTelefon
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.core.files.base import ContentFile
from base64 import b64decode
import uuid
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def rehber_index(request):
    kisiler = Kisi.objects.all()
    contex = {
        'kisiler': kisiler,
    }
    return render(request, "rehber/index.html", contex)


def test(request):
    a = 'fatih'

    return HttpResponse(a)


def get_kisi_telefonlari(request):
    kisitelefonlari = Kisi.objects.get(KisiID=request.POST['KisiID']).Telefons.all()
    data = serializers.serialize('json', kisitelefonlari)
    return HttpResponse(data, content_type='application/json', )


@api_view(['GET', 'POST'])
def kisiler(request):
    if request.method == 'GET':
        kisiler = Kisi.objects.all()
        serializer = kisiSerializer(kisiler, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = kisiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def kisilerekle(request):
    try:
        if request.method == 'POST':
            data = JSONParser().parse(request)

            for item in data:

                kisitelefon = item.get('KisiTelefon')
                serializerkisitelefon = kisiTelefonSerializer(data=kisitelefon)
                serializerkisitelefon.is_valid()

                kisitelefonmodel = KisiTelefon.objects.filter(Telefon=serializerkisitelefon.data.get('Telefon')).first()

                if kisitelefonmodel:
                    kisitelefonmodel.Telefon = serializerkisitelefon.data.get('Telefon')
                    kisitelefonmodel.Tur = serializerkisitelefon.data.get('Tur')
                    kisitelefonmodel.save()

                    kisi = item.get('Kisi')
                    serializerKisi = kisiSerializer(data=kisi)
                    if serializerKisi.is_valid():
                        kisimodel = kisitelefonmodel.Kisi
                        kisimodel.Adi = serializerKisi.data.get('Adi')
                        kisimodel.Soyadi = serializerKisi.data.get('Soyadi')

                        resimadi = 'resim%s@2x.jpeg' % (uuid.uuid4().hex[:6].upper())
                        image_data = b64decode(kisi.get('Resim64'))
                        kisimodel.Resim = ContentFile(image_data, resimadi)
                        kisimodel.save()

                else:
                    kisi = item.get('Kisi')

                    kisitelefonmodel = KisiTelefon()

                    kisimodel = Kisi.objects.filter(Adi=kisi.get('Adi'),
                                                    Soyadi=kisi.get('Soyadi'), ).first()
                    if kisimodel:
                        kisitelefonmodel.Kisi_id = kisimodel.KisiID
                    else:
                        serializerKisi = kisiSerializer(data=kisi)
                        if serializerKisi.is_valid():
                            serializerKisi.save()
                            kisitelefonmodel.Kisi_id = serializerKisi.data.get('KisiID')

                    kisitelefonmodel.Telefon = serializerkisitelefon.data.get('Telefon')
                    kisitelefonmodel.Tur = serializerkisitelefon.data.get('Tur')
                    kisitelefonmodel.save()

            return Response(data, status=status.HTTP_201_CREATED)

    except Exception as ex:
        return Response("Hatalı %s" % (ex), status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def kisisil(request):
    try:
        if request.method == 'DELETE':
            try:
                kisi = Kisi.objects.get(KisiID=request.POST['KisiID'])
            except ObjectDoesNotExist:
                kisi = None

            if kisi:
                kisi.delete()
                return Response({'Sonuc': 'Başarılı', 'KOD': 200}, status=status.HTTP_200_OK)
            else:
                return Response({'Sonuc': 'Kişi Bulunamadı', 'KOD': 404}, status=status.HTTP_200_OK)


    except Exception as ex:
        return Response({'Sonuc': 'Başarılı'}, status=status.HTTP_400_BAD_REQUEST)


class KisiList(APIView):
    def get(self, request):
        kisiler = Kisi.objects.all()
        serializer = kisiSerializer(kisiler, many=True)
        return Response(serializer.data)

    def post(self, request):
        kisitelefonlari = Kisi.objects.get(KisiID=1)
        data = serializers.serialize('json', kisitelefonlari)
        return Response(data)
