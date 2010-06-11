from django.contrib import admin

from panya.admin import ModelBaseAdmin
from event.models import Appearance, Event, Location, Venue

class AppearanceInline(admin.TabularInline):
    model = Appearance

class EventAdmin(ModelBaseAdmin):
    inlines = [
        AppearanceInline,
    ]
    
admin.site.register(Event, EventAdmin)
admin.site.register(Location)
admin.site.register(Venue)
