from api import views
from django.conf.urls import patterns, url, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'research_session', views.ResearchSessionViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
