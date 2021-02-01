"""my_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    #auth
    path('login/', views.login1, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name='logout'),
    ##criminal
    path('criminal/', views.criminal, name="criminal"),
    path('create', views.insert, name="insert"),
    path('update/<int:id>', views.update, name="update"),
    path('criminal/<int:id>', views.requpdate, name="requpdate"),
    path('delete/<int:id>', views.crdel, name="crdel"),
    ##officer
    path('officer/', views.officerClass, name="officer"),
    path('createofficer/', views.insertofficer, name="insertofficer"),
    # path('updateofficer/<int:id>', views.updateofficer, name="updateofficer"),
    # path('updateMeofficer/<int:id>', views.requpdateofficer, name="requpdateofficer"),
    path('deleteofficer/<int:id>', views.crdelofficer, name="crdelofficer"),
    ##fir
    path('fir/', views.firClass, name="fir"),
    path('createfir/', views.insertfir, name="insertfir"),
    # path('updatefir/<int:id>', views.updatefir, name="updatefir"),
    # path('updateMefir/<int:id>', views.requpdatefir, name="requpdatefir"),
    path('deletefir/<int:id>', views.crdelfir, name="crdelfir"),
]