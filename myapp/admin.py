from django.contrib import admin

from myapp.models import Project, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
# admin.site.register(Task)