from api.models import Document, Question, ResearchSession, Page
from django.contrib import auth
from rest_framework import serializers

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'publish_date')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'document')


class ResearchSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchSession


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auth.get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email',
                  'groups', 'is_active', 'last_login', 'date_joined')


class PageSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.CharField(required=False)
    class Meta:
        model = Page
        fields = ('page_url', 'title', 'content', 'website', 'research_session')
