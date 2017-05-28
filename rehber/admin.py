from django.contrib import admin
from .models import Kisi,KisiTelefon,KisiEposta


# Register your models here.

class KisiAdmin(admin.ModelAdmin):
    list_display = ['Adi', 'Soyadi']

    class Meta:
        model = Kisi

class KisiTelefonAdmin(admin.ModelAdmin):
    list_display = ['Telefon','Kisi']

    class Meta:
        model = Kisi

class KisiEpoataAdmin(admin.ModelAdmin):
    list_display = ['Eposta','Kisi']

    class Meta:
        model = Kisi

admin.site.register(Kisi, KisiAdmin)
admin.site.register(KisiTelefon, KisiTelefonAdmin)
admin.site.register(KisiEposta, KisiEpoataAdmin)