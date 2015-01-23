from django.db import models
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import eyed3

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class Metadata(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=255, blank=True, null=True)
    album = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    trackNumber = models.IntegerField(blank=True, null=True)
    length = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return self.title + ' - ' + self.artist + ' - ' + self.album

class Track(models.Model):
    filename = models.CharField(max_length=255, blank=True)
    file = models.FileField()
    date_create = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User)
    metadata = models.ForeignKey(Metadata, null=True)

    def __unicode__(self):
        return self.filename

    def delete(self, *args, **kwargs):
        storage, path = self.file.storage, self.file.path
        metadata = self.metadata
        super(Track, self).delete(*args, **kwargs)
        metadata.delete(*args, **kwargs)
        storage.delete(path)

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    date_create = models.DateField(auto_now_add=True)
    tracks = models.ManyToManyField(Track)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class LastPlaylist(models.Model):
    playlist = models.ForeignKey(Playlist)
    owner = models.ForeignKey(User)
    def __unicode__(self):
        return str(self.owner) + ' - ' + self.playlist.__unicode__()