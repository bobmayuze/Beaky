from django.urls import path

from . import views

urlpatterns = [
    path('signUp', views.signUp),
    path('', views.index, name='index'),
]
