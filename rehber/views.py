import json
from django.shortcuts import render, HttpResponse
from .models import Kisi, KisiEposta, KisiTelefon
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import rehberSerializer

# Create your views here.
def rehber_index(request):
    kisiler = Kisi.objects.all()
    contex = {
        'kisiler': kisiler,
    }
    return render(request, "rehber/index.html", contex)

def test(request):
    a = 'fatih';

    return HttpResponse(a)

def get_kisi_telefonlari(request):
    kisitelefonlari = Kisi.objects.get(KisiID=request.POST['KisiID']).Telefons.all()
    data = serializers.serialize('json', kisitelefonlari)
    return HttpResponse(data, content_type='application/json',)


class KisiList(APIView):

    def get(self, request):
        kisiler = Kisi.objects.all()
        serializer = rehberSerializer(kisiler, many=True)
        return Response(serializer.data)

    def post(self):
        pass
