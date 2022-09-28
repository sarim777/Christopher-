"""nolan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from nolanapp import views
from account import views as ac

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,views.index,name="index.html"),
    path('<id>',views.detail,name='detail.html'),
    path('add/',views.add_movie,name="add_movie.html"),
    path('imdb/',views.imdb,name="imdb.html"),
    path('update/<id>',views.update,name="upadte.html"),
    path('delete/<id>',views.delete,name="delete.html"),
    path('account/login/',ac.login,name="login.html"),
    path('account/register/',ac.register,name="register.html"),
]
