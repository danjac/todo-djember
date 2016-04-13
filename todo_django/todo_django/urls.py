"""todo_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from todo.views import TodoItemViewSet
from .views import register

# we need to make trailing_slash False to work with EmberData
router = routers.DefaultRouter(trailing_slash=False)
router.register("todos", TodoItemViewSet, base_name='todo')

urlpatterns = [
    url(r'^api-auth-token/', obtain_auth_token),
    url(r'^api-register/', register),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
