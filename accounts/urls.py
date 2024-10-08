from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import RegisterView, CustomLoginView, CustomLogoutView, GoogleAuthCompleteView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('google-auth-complete/', GoogleAuthCompleteView.as_view(), name='google_auth_complete'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
