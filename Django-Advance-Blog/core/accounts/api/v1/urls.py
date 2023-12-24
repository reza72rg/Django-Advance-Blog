from django.urls import path,include
from .views import RegisterApiViews
app_name = 'api-v1'

urlpatterns = [
    path("register/", RegisterApiViews.as_view(), name="register"),
   
]