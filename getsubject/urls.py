from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getsubject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'subject.views.search', name='home'),
    url(r'^about/', 'subject.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
