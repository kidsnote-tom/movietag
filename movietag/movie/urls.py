from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movietag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.movie_list, name='movie_lsit'),
)
