from django.contrib import admin

from .models import Airport, Flight, Passenger
# Register your models here.

# this is going to do is to tell Django's admin app that I would like to use the
# admin app to be able to manipulate airports and to be able to manipuldate flights as well
# Django' admin ; admin app;manipuldate airports;manipuldate flights

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
