import eyed3
from iom.settings import MEDIA_ROOT
from os.path import join
from player.models import Metadata, LastPlaylist

def none_check(value, replace=''):
    if value is None:
        return replace
    else:
        return value

def read_metadata(filename):
    filename = join(MEDIA_ROOT, filename)
    audiofile = eyed3.load(filename)
    if audiofile is None:
        return None
    tag = audiofile.tag
    duration = audiofile.info.time_secs
    time = ':'.join([str(i) for i in [duration // 60, duration % 60]])
    meta = Metadata(
        title=none_check(tag.title),
        artist=none_check(tag.artist),
        album=none_check(tag.album),
        trackNumber = none_check(tag.track_num[0]) or None,
        genre = none_check(tag.genre),
        length = time
    )
    return meta

def set_last_playlist(user, playlist):
    try:
        last = LastPlaylist.objects.get(owner=user)
        last.playlist = playlist
    except LastPlaylist.DoesNotExist:
        last = LastPlaylist(playlist=playlist, owner=user)
    last.save()