from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Places)
admin.site.register(BusChart)
admin.site.register(BusTrip)