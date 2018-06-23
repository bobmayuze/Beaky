from django.urls import path

from . import views

urlpatterns = [
    path('publish', views.publish),
    path('vote', views.vote),
    path('getQuestionById', views.searchQuestionById),
    path('getQuestionByLabels', views.searchQuestionByLabels),
    path('', views.index, name='index'),
]
