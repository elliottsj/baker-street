from api.models import Document, Question, ResearchSession
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
