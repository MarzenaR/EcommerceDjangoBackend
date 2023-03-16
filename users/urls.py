from django.urls import path, include

from users.views import RegisterUserView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterUserView.as_view()),
]