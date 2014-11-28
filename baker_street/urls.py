from django.contrib import admin
from django.views.generic.base import RedirectView
from baker_street import views
from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework_nested import routers as r

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'research_session', views.ResearchSessionViewSet)
router.register(r'pages', views.PageViewSet)

research_session_router = r.NestedSimpleRouter(router, r'research_session', lookup='research_session')
research_session_router.register(r'sitelist', views.SitelistViewSet)


urlpatterns = patterns('',
    # Redirect root path to marketing site
    url(r'^$', RedirectView.as_view(url='https://www.sherlocke.me', permanent=False)),

    # Include the routes registered above
    url(r'^', include(router.urls)),

    url(r'^', include(research_session_router.urls)),

    # Include routes for logging into the generated documentation site
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Include OAuth2 routes
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # User dashboard page
    url(r'^dashboard/', views.dashboard, name='dashboard'),

    # Admin panel
    url(r'^admin/', include(admin.site.urls)),
)
