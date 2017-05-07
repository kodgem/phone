from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'rehber'

urlpatterns = [
    url(r'^index/$', rehber_index, name='index'),
    url(r'^test/$', test, name='test'),
    url(r'^get_kisi_telefonlari/$', get_kisi_telefonlari, name='get_kisi_telefonlari'),
    url(r'^api/$', KisiList.as_view(), name='api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)