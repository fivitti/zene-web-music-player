from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from forms import TrackForm, MetadataForm, MultiTracksForm, MultiPlaylistForm
from player.models import Track, Metadata, Playlist, LastPlaylist
import datetime
from os.path import basename
from iom.helpers import group_required
from player.helpers import set_last_playlist, read_metadata

# Create your views here.
@login_required
@group_required('normal')
def player(request):
    try:
        last = LastPlaylist.objects.get(owner=request.user)
        tracks = last.playlist.tracks.all()
        dict = {'tracks': tracks}
    except:
        dict = {}
    return render(request, 'player/player.html', dict)

@login_required
@group_required('normal')
def add_file(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            file_=cleaned_data.get('file')
            # meta = read_metadata(file)
            # meta.save()
            track = Track(filename='temp',
                          file=file_,
                          date_create=datetime.datetime.now().date(),
                          owner=request.user,
                          # metadata=Metadata())
            )
            track.save()
            track.filename = basename(track.file.name)
            meta = read_metadata(track.file.name)
            if meta is not None:
                meta.save()
                track.metadata = meta
            track.save()
            return redirect('player.views.files')
    else:
        form = TrackForm()
    return render(request, 'player/add_file.html', {'form': form})

@login_required
@group_required('normal')
def files(request):
    errors = ''
    if request.method == 'POST':
        form = MultiTracksForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data['choices']
            if 'delete' in request.POST:
                for item in items:
                    item.delete()
            if 'playlist' in request.POST:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # playlist = Playlist(title=now)
                playlist = Playlist(name=now, owner=request.user)
                playlist.save()
                for item in items:
                    playlist.tracks.add(item)
                set_last_playlist(request.user, playlist)
                return redirect('player.views.player')
        else:
            errors = 'Nie wybrano pliku.'

    track_user = Track.objects.filter(owner=request.user)
    return render(request, 'player/files.html', {'tracks': track_user, 'errors':errors})

@login_required
@group_required('normal')
def playlists(request):
    errors = ''
    if request.method == 'POST':
        form = MultiPlaylistForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data['choices']
            if 'delete' in request.POST:
                for item in items:
                    item.delete()
            if 'playlist' in request.POST:
                playlist = items[0]
                set_last_playlist(request.user, playlist)
                return redirect('player.views.player')
        else:
            errors = 'Nie wybrano pliku.'

    playlists_user = Playlist.objects.filter(owner=request.user)
    return render(request, 'player/playlists.html', {'playlists': playlists_user, 'errors':errors})

@login_required
@group_required('normal')
def detail(request, t_id):
    if request.method == 'POST':
        metadata = get_object_or_404(Metadata, id=t_id)
        form = MetadataForm(request.POST, instance=metadata)
        if form.is_valid():
            form.save()
        return redirect('player.views.files')

    track = get_object_or_404(Track, id=t_id)
    metadata = track.metadata
    form = MetadataForm(instance=metadata)
    return render(request, 'player/metadata.html', {'form': form, 'm_id':metadata.id})