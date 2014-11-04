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


class ResearchSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResearchSession
        fields = ('question_text', 'document')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auth.get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email',
                  'groups', 'is_active', 'last_login', 'date_joined')

class PageSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.Field(required=False)
    website = serializers.Field(required=False)
    class Meta:
        mode = Page
        fields = ('url', 'title', 'content', 'False')
