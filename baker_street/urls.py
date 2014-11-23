from django.contrib import admin
from django.views.generic.base import RedirectView
from baker_street import views
from django.conf.urls import patterns, url, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'research_session', views.ResearchSessionViewSet)
router.register(r'pages', views.PageViewSet)
router.register(r'blacklist', views.BlacklistViewSet)

urlpatterns = patterns('',
    # Redirect root path to marketing site
    url(r'^$', RedirectView.as_view(url='https://www.sherlocke.me', permanent=False)),

    # Include the routes registered above
    url(r'^', include(router.urls)),

    # Include routes for logging into the generated documentation site
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # User dashboard page
    url(r'^dashboard/', views.dashboard, name='dashboard'),

    # Admin panel
    url(r'^admin/', include(admin.site.urls)),
)
