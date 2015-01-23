# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

STATUSES = (
    ('a', 'Awating'),
    ('s', 'Settled'),
)
class Application(models.Model):
    title = models. CharField(max_length=64)
    user = models.ForeignKey(User, related_name='Zglaszany')
    description = models.CharField(max_length=255)
    answer = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, related_name='Autor')
    status = models.CharField(max_length=1, choices=STATUSES)
    date_create = models.DateField()

    def __unicode__(self):
        return self.title + ' - ' + str(self.author)