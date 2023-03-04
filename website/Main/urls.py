from django.urls import path
from  . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

]
