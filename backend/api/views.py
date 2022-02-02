# from django.shortcuts import render
from blog.models import Article
from api.serializers import ArticleSerializer, UserSerializer
# from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from api.permissions import IsSuperUser , IsAuthorOrReadOnly , IsStaffOrReadOnly , IsSuperuserOrStaffReadOnly
# from rest_framework.views import APIView
# from rest_framework.response import Response

# Create your views here.

# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetail(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

# class ArticleDestroy(RetrieveDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleUpdate(RetrieveUpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDeleteUpdate(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsStaffOrReadOnly,IsAuthorOrReadOnly)

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['status', 'author__username']
    ordering_fields = ['publish','status']
    ordering = ['-publish']
    search_fields = [
        'title',
        'content',
        'author__username',
        'author__first_name',
        'author__last_name',
    ]
    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)

    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         queryset = queryset.filter(author__username=author)
            
    #     return queryset

    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly,IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperuserOrStaffReadOnly,)    

# class UserDeleteUpdate(RetrieveUpdateDestroyAPIView):
#     # def get_queryset(self):
#     #     print('----------------------')
#     #     print(self.request.auth)
#     #     print(self.request.user)
#     #     print('----------------------')
#     #     return User.objects.all
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperuserOrStaffReadOnly,)

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
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