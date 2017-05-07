from django.contrib import admin
from .models import Kisi,KisiTelefon


# Register your models here.

class KisiAdmin(admin.ModelAdmin):
    list_display = ['Adi', 'Soyadi']

    class Meta:
        model = Kisi

class KisiTelefonAdmin(admin.ModelAdmin):
    list_display = ['Telefon']

    class Meta:
        model = Kisi

admin.site.register(Kisi, KisiAdmin)
admin.site.register(KisiTelefon, KisiTelefonAdmin)