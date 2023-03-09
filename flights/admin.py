from django.contrib import admin

# Register your models here.
from .models import Flight, Airport, Passenger

class FlightAdmin(admin.ModelAdmin):
  list_display = ("id", "origin", "destination", "duration")   # list_display is in Django docs

class PassengerAdmin(admin.ModelAdmin):
  filter_horizontal = ("flights", )   # a way to show many-to-many relations.. filter_horizontal is in Django docs

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin) #register Flight model, but use FlightAdmin settings
admin.site.register(Passenger, PassengerAdmin) #register Passenger, but use PassengerAdmin settings
