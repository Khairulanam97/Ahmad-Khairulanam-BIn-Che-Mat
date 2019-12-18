from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
        path('', views.home, name="home"),
        path('stock', views.stock, name="stock"),
        path('login2', views.login2, name="login2"),
        path('register', views.register, name="register"),
        path('addmedi', views.addmedi, name="addmedi"),
        ]