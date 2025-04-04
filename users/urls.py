from django.urls import path
from .views import UserLoginView, RegisterView, logout_user

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
    # path('dashboard/', DashboardView.as_view(), name='dashboard'),  # Dashboard page
]