from django.contrib import admin

from .models import *

admin.site.register(Planet)
admin.site.register(Astronaut)
admin.site.register(Expedition)