from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^api/', include('api.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='https://www.sherlocke.me'))
)
