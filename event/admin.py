from django.contrib import admin

from content.admin import ModelBaseAdmin
from event.models import Event, Location, Venue

class VenueInline(admin.TabularInline):
    model = Venue

class EventAdmin(ModelBaseAdmin):
    inlines = [
        VenueInline,
    ]
    
admin.site.register(Event, EventAdmin)
admin.site.register(Location)
