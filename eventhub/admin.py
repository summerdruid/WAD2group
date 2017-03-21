from django.contrib import admin
from eventhub.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'loc', 'creator', 'datetime', 'id', 'desc', 'pos')

admin.site.register(Event, EventAdmin)

# Register your models here.
