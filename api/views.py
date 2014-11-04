from api.models import Document, Question
from api.serializers import DocumentSerializer, QuestionSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets


class DocumentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows documents to be viewed or edited"""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
