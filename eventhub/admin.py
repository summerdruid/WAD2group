from django.contrib import admin
from eventhub.models import Event, Pref, Like

class EventAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'loc', 'creator', 'datetime', 'id', 'desc', 'pos', 'likes')

class PrefAdmin(admin.ModelAdmin):
    list_display = ('user', 'preference')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')

admin.site.register(Event, EventAdmin)
admin.site.register(Pref, PrefAdmin)
admin.site.register(Like, LikeAdmin)

# Register your models here.
