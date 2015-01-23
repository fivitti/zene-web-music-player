# -*- coding: utf-8 -*-
from django import forms
from player.models import Track, Metadata, Playlist

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        exclude = ('filename', 'owner', 'metadata', 'date_create')
    def __init__(self, *args, **kwargs):
        super(TrackForm, self).__init__(*args, **kwargs)
        self.fields['file'].label = "Wybierz plik"

class MetadataForm(forms.ModelForm):
    class Meta:
        model = Metadata
        exclude = ('length', )
    def __init__(self, *args, **kwargs):
        super(MetadataForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Tytuł"
        self.fields['artist'].label = "Artysta"
        self.fields['album'].label = "Album"
        self.fields['genre'].label = "Gatunek"
        self.fields['trackNumber'].label = "Numer ścieżki"

class MultiTracksForm(forms.Form):
    choices = forms.ModelMultipleChoiceField(
        queryset = Track.objects.all(), # not optional, use .all() if unsure
        widget = forms.CheckboxSelectMultiple,
    )

    def clean(self):
        cleaned_data = super(MultiTracksForm, self).clean()
        try:
            cleaned_data['choices']
        except KeyError:
            raise forms.ValidationError('Nie wybrano pliku.')

class MultiPlaylistForm(forms.Form):
    choices = forms.ModelMultipleChoiceField(
        queryset = Playlist.objects.all(), # not optional, use .all() if unsure
        widget = forms.CheckboxSelectMultiple,
    )