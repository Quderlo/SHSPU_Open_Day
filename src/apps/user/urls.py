from django.urls import path, include
from apps.user.views.login import LoginView
from django.contrib.auth.views import LogoutView

from apps.user.views.registration import RegistrationView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]