from django.contrib import admin
from .models import ActiveOutage,ArchiveOutage

# Register your models here.
admin.site.register(ActiveOutage)
admin.site.register(ArchiveOutage)