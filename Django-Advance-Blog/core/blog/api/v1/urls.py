from django.urls import path,include
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostListModuleSet, basename='post')
router.register('category', CategoryListModuleSet, basename='category')
urlpatterns = router.urls

app_name = 'api-v1'
'''
urlpatterns = [
    # path('post/',PostList.as_view(), name ='post-list'),
    # path('post/<int:pk>/',PostDetail.as_view(), name ='post-detail'),
    path('post/',PostListViewSet.as_view({'get':'list','post':'create'}), name ='post-list'),
    path('post/<int:pk>/',PostListViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name ='post-detail'),
    
]'''