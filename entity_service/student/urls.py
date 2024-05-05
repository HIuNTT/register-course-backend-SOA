from django.urls import path
from rest_framework_simplejwt import views

from .views import RegisterStudentAPIView

urlpatterns = [
    path('login', views.TokenObtainPairView.as_view()),
    path('login/refresh', views.TokenRefreshView.as_view()),
    path('register', RegisterStudentAPIView.as_view()),
]
