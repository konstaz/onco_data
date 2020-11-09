from django.urls import path

from account import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'account'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my_profile/<int:pk>/', views.MyProfile.as_view(), name='my_profile'),
    path('password_change/<int:pk>/', views.ChangePassword.as_view(), name='password_change'),
    path('sign-up/', views.SignUp.as_view(), name='sign-up'),

]
