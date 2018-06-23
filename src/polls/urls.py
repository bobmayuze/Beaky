from django.urls import path

from . import views

urlpatterns = [
    path('page', views.foo),
    path('', views.index, name='index'),
]