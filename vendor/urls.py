from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginVendor, name='loginVendor'),
    # path('', views.homepage , name='homepage'),
    path('register/', views.createVendor, name='registerVendor'),
    path('logout/', views.logoutVendor, name='logoutVendor'),
    path('newview/', views.newview),
    path('shopview/<str:pk>/', views.shopview, name='shopview'),
    # # path('accounts/password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # # path('profile/', views.customer_profile, name='customerprofile'),
    # # path('editprofile/', views.edit_profile, name='editprofile'),
    # # path(),


]