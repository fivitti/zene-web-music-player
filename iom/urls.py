from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from iom.settings import MEDIA_ROOT

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'iom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^player/', include('player.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mod/', include(admin.site.urls)),
    url(r'^org/', include('org.urls')),
    url(r'^logout/', 'iom.views.logout_view'),
    url(r'^start/', include('reg.urls')),
    url(r'^$', 'iom.views.index'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
