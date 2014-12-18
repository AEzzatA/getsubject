from django.conf.urls import patterns, include, url
from django.contrib import admin
from subject import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getsubject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', views.search)
)
