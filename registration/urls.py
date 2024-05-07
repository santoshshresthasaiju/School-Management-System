from django.urls import path, include
from . import views

urlpatterns = [
    path('home',views.homepage, name="home"),
    path('', views.login_view, name="login"), 
    path('logout/', views.logout_view, name="logout"),
    path ('register/',views.register_view,name='register'),
]
