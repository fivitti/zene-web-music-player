from django.conf.urls import patterns, include, url
import django.contrib.auth

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^org/', 'reg.views.org'),
    url(r'^login/', 'reg.views.login_my'),
    url(r'^register/', 'reg.views.register_my'),
    url(r'^$', 'reg.views.index'),
)