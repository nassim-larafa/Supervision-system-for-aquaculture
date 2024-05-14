from django.contrib import admin
from django.contrib.gis import admin
from .models import node, myProject, parcelle, Data



admin.site.register(Data)
admin.site.register(parcelle)
admin.site.register(node)
admin.site.register(myProject)
class polygonAdmin(admin.GISModelAdmin):
    list_display = ("geom")

class myProjectAdmin(admin.ModelAdmin):
    list_display = ['polygon_id', 'nomp', 'descp', 'debutp', 'finp', 'cityp', 'clientp']

