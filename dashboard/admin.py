from django.contrib import admin
from .models import Locations, Events, Response

# Register your models here.
admin.site.register(Locations)
admin.site.register(Events)
admin.site.register(Response)
