# from django.shortcuts import render
from urllib import response
from blog.models import Article
from api.serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from api.permissions import IsSuperUser , IsAuthorOrReadOnly , IsStaffOrReadOnly , IsSuperuserOrStaffReadOnly
# from rest_framework.views import APIView
# from rest_framework.response import Response

# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

class ArticleDestroy(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleUpdate(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDeleteUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly,IsAuthorOrReadOnly)

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)    

class UserDeleteUpdate(RetrieveUpdateDestroyAPIView):
    # def get_queryset(self):
    #     print('----------------------')
    #     print(self.request.auth)
    #     print(self.request.user)
    #     print('----------------------')
    #     return User.objects.all
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)

'''
class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     return Response({'method':'get'})

    # def post(self, request):
    #     return Response({'method':'post'})

    # def put(self, request):
    #     return Response({'method':'put'})

    def delete(self, request):
        request.auth.delete()
        return Response(status=204)
'''