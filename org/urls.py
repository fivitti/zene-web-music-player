from django.conf.urls import patterns, include, url
import django.contrib.auth

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'org.views.awaiting'),
    url(r'^settled/', 'org.views.settled'),
    url(r'^new/', 'org.views.new_application'),
    url(r'^application/(?P<app_id>\d+)/','org.views.detail')
)