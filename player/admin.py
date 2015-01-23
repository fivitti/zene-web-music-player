from django.contrib import admin
from models import Metadata, Track, Playlist, LastPlaylist
# Register your models here.
admin.site.register(Metadata)
admin.site.register(Track)
admin.site.register(Playlist)
admin.site.register(LastPlaylist)