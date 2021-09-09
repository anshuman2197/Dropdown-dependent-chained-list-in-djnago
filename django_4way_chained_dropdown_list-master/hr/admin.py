from django.contrib import admin

# Register your models here.

from .models import Location, Section, Unit, Project , Person




admin.site.register(Location)
admin.site.register(Section)
admin.site.register(Person)
admin.site.register(Unit)
admin.site.register(Project)