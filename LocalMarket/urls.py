from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginUser, name='loginUser'),
    path('', views.homepage , name='homepage'),
    path('register/', views.createUser, name ='registerUser'),
    path('logout/', views.logoutUser, name = 'logoutUser'),
    path('accounts/password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('profile/', views.customer_profile, name='customerprofile'),
    path('editprofile/', views.edit_profile, name='editprofile'),
    # path(),


]