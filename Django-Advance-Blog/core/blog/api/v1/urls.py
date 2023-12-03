from django.urls import path,include
from .views import * 
app_name = 'api-v1'

urlpatterns = [
    path('post/',PostList, name ='post-list'),
    path('post/<int:id>/',PostDetail, name ='post-detail'),
 
    
]