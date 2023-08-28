from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('register/', UserRegister,name="register"),
    path('login/', UserLogin,name="login"),
    path('logout/', UserLogout,name="logout"),
]