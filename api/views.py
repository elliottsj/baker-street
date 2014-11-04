from api.models import Document, Question, Page, ResearchSession
from api.serializers import DocumentSerializer, QuestionSerializer, UserSerializer, PageSerializer, ResearchSessionSerializer
from django.contrib import auth
from rest_framework import permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response


class DocumentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows documents to be viewed or edited"""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for user """
    queryset = auth.get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # POST /users/sign_in.json
    @list_route(methods=['POST'])
    def sign_in(self, request, format=None):
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({
            'user': request.user
        })

    # POST /users/register.json
    @list_route(methods=['POST'])
    def register(self, request, format=None):
        pass

    # DELETE /users/sign_out.json
    @list_route(methods=['DELETE'])
    def sign_out(self, request, format=None):
        pass

class ResearchSessionViewSet(viewsets.ModelViewSet):
    queryset = ResearchSession.objects.all()
    serializer_class = ResearchSessionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, format=None):
        session = request.user.researchsession_set.create()
        serializer = ResearchSessionSerializer(session)
        return Response(serializer.data)

    @detail_route(methods='GET')
    def pages(self, request, format=None):
        pass

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, format=None):
        serializer = PageSerializer(request.DATA)
