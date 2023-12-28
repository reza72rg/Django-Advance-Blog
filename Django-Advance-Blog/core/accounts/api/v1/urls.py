from django.urls import path,include
from .views import RegisterApiViews, CustomAuthToken, CustomDiscardAuthToken
#from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api-v1'
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    
    path("register/", RegisterApiViews.as_view(), name="register"),
    path("token/login/", CustomAuthToken.as_view(), name="token-login"),
    path("token/logout/", CustomDiscardAuthToken.as_view(), name="token-logout"),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/token/verify/', TokenVerifyView.as_view(), name='jwt_verify'),

   
]