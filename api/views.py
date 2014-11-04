from api.models import Document, Question, Page, ResearchSession
from api.serializers import DocumentSerializer, QuestionSerializer, UserSerializer, PageSerializer, \
    AuthTokenSerializer, ResearchSessionSerializer
from django.contrib import auth
from rest_framework import mixins, renderers, permissions, views, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import list_route, detail_route
from rest_framework import generics
from rest_framework.response import Response
from pycanlii.canlii import CanLII
from api.scooby_doo.canlii_document import CanLIIDocument
from django.http import JsonResponse


# class DocumentViewSet(viewsets.ModelViewSet):
#     """API endpoint that allows documents to be viewed or edited"""
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer
#
#
# class QuestionViewSet(viewsets.ModelViewSet):
#     """API endpoint that allows groups to be viewed or edited"""
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer


class AuthViewSet(viewsets.ModelViewSet):
    queryset = auth.get_user_model().objects.all()
    serializer_class = AuthTokenSerializer

    # POST /users/sign_in.json
    @list_route(methods=['POST'])
    def sign_in(self, request, format=None):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.object['user'])
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # POST /users/register.json
    # @list_route(methods=['POST'])
    # def register(self, request, format=None):
    #     pass

    # DELETE /users/sign_out.json
    @list_route(methods=['DELETE'], permission_classes=[permissions.IsAuthenticated])
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

    @detail_route(methods=["GET"])
    def documents(self, request, pk=None):
        #page_num = request.QUERY_PARAMS["page"]
        #page = Page.objects.get(pk=page_num)

        canlii = CanLII("5tt8fdbp4s5jqjsj7arvfgbj")
        dbs = canlii.case_databases()
        db = dbs[0]
        s = []
        for x in range(20):
            s.append(CanLIIDocument(db[x]).json())



        return JsonResponse(s, safe=False)


    @detail_route(methods=['POST'])
    def pages(self, request, format=None, pk=None):
        if request.method == "POST":
            session = ResearchSession.objects.get(pk=pk)
            page = PageSerializer(data=request.DATA)
            session.page_set.add(page)
            page.save()
            return Response(page.data, status=status.HTTP_201_CREATED)

