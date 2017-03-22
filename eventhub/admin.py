from django.contrib import admin
from eventhub.models import Event, Pref

class EventAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'loc', 'creator', 'datetime', 'id', 'desc', 'pos', 'likedBy')

class PrefAdmin(admin.ModelAdmin):
    list_display = ('user', 'preference')

admin.site.register(Event, EventAdmin)
admin.site.register(Pref, PrefAdmin)

# Register your models here.
