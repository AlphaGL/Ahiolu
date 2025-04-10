from django.urls import path
from .views import UserLoginView, RegisterView, logout_user,user_dashboard,UserUpdateView,UserDeleteView

# reset password
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    # user dashboard
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('profile/edit/', UserUpdateView.as_view(), name='user-update'),
    path('profile/delete/', UserDeleteView.as_view(), name='user-delete'),

    # reset password views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]