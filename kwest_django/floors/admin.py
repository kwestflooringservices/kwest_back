from django.contrib import admin
from .models import Floor

# Register your models here.
@admin.register(Floor)
class AdminFloor(admin.ModelAdmin):
    list_display = [field.name for field in Floor._meta.get_fields()]