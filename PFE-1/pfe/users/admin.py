from django.contrib import admin
from users.models import *

# Register your models here.
class clientAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','NB_GSM','pseudo','e_mail')

class supervisorAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','NB_GSM','pseudo','e_mail')


admin.site.register(client,clientAdmin)
admin.site.register(supervisor,supervisorAdmin)
