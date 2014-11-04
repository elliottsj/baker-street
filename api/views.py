from api.models import Document, Question
from api.serializers import DocumentSerializer, QuestionSerializer, UserSerializer
from django.contrib import auth
from rest_framework import permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import list_route
from rest_framework.response import Response


class DocumentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows documents to be viewed or edited"""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UserViewSet(viewsets.GenericViewSet):
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
