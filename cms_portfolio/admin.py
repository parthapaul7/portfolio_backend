from django.contrib import admin
from . import models
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Project, ProjectAdmin)
