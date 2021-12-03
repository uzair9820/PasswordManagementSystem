from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='index'),
    path('signup', views.signup, name="signup"),
    path('generator',views.generator, name="generator"),
    path('manager',views.manager,name="manage"),
    path('generate',views.generate, name="generate"),
    path('copy',views.copy,name="copy"),
    path('signin',views.signin,name="signin"),
    path('postsignin',views.postsignin,name="postsignin"),
    path('postsignup',views.postsignup,name="postsignup"),
    path('logout',views.logout,name="logout"),
    path('add',views.add,name="add"),
    path('delete',views.delete,name="delete"),
    path('showsaveddata',views.showsaveddata,name="showsaveddata"),
    path('hidesaveddata',views.hidesaveddata,name="hidesaveddata"),
]