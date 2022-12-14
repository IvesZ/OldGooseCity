"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views


router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')
router.register(r'users', views.userView, 'user')


urlpatterns = [
    path('hello/', views.hello),
    path('/', admin.site.urls),
    path('api/', include(router.urls)),
    path('apiv2/login', views.login),
    path('apiv2/register', views.register),
    path('addcart/', views.add_cart),
    path('rmcart/', views.remove_cart),
    path('getshoppingcard/', views.get_chopping_card),

]
