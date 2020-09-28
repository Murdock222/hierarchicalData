from django.contrib import admin
from mpttapp.models import Folder
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
# Register your models here.
admin.site.register(Folder, DraggableMPTTAdmin)