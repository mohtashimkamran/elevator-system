from django.contrib import admin
from .models import Elevator
# Register your models here.

# admin.site.register(article)

@admin.register(Elevator)
class articleAdmin(admin.ModelAdmin):
    list_display = ['id','name','floors']
