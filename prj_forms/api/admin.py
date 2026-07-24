from django.contrib import admin
from .models import dataClass


# Register your models here.

@admin.register(dataClass)
class dataClassAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'email', 'date')