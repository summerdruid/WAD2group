from django.contrib import admin
from eventhub.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'loc', 'creator', 'date', 'time', 'id')

admin.site.register(Event, EventAdmin)

# Register your models here.
