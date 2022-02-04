from django.urls import path , include
# from .views import ArticleDestroy, ArticleList, ArticleDetail, ArticleUpdate,ArticleDeleteUpdate,UserList,UserDeleteUpdate
from rest_framework import routers
from .views import ArticleViewSet, UserViewSet #, AuthorRetrieve
app_name = 'api'

# urlpatterns = [
#     path('', ArticleList.as_view(), name='list'),
#     path('<slug:slug>', ArticleDetail.as_view(), name='detail'),
#     path('delete/<int:pk>', ArticleDestroy.as_view(), name='delete'),
#     path('update/<int:pk>', ArticleUpdate.as_view(), name='update'),
#     path('edit/<int:pk>', ArticleDeleteUpdate.as_view(), name='edit'),
#     path('users/', UserList.as_view(), name='user-list'),
#     path('users/<int:pk>', UserDeleteUpdate.as_view(), name='user-edit'),
# ]


router = routers.SimpleRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet, basename='users')
# urlpatterns = router.urls

urlpatterns =[
    path('',include(router.urls)),
    # path('authors/<int:pk>/',AuthorRetrieve.as_view(), name='authors_detail'),

]