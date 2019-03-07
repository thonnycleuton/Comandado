from django.contrib import admin
from .models import Agenda


# Register your models here.
class AgendaAdmin(admin.ModelAdmin):
    list_display = ['customer', 'start_time', 'end_time']


admin.site.register(Agenda)
