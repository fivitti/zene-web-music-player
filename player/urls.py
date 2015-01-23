from django.conf.urls import patterns, include, url
import django.contrib.auth
from iom import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'player.views.player'),
    url(r'^files/', 'player.views.files'),
    url(r'^add/', 'player.views.add_file'),
    url(r'^playlists', 'player.views.playlists'),
    url(r'^track/(?P<t_id>\d+)/','player.views.detail')
  #  url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': ''})

)