from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^theblog/index/$', 'theblog.views.index'),
)
