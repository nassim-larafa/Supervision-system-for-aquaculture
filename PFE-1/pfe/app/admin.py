from django.contrib import admin
from django.contrib.gis import admin
from .models import node
from .models import polygon


class polygonAdmin(admin.GISModelAdmin):
    list_display = ('name','poly')

class nodeAdmin(admin.ModelAdmin):
    list_display = ('name','location')


admin.site.register(polygon, polygonAdmin)
admin.site.register(node, nodeAdmin)
