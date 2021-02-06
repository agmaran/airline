from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.


class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


class PassengerAdmin(admin.ModelAdmin):
    # Special way of manipulating many to many relationships
    # This will just make it a little bit nicer for manipulating
    filter_horizontal = ("flights",)


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
