from django.urls import path

from . import views

urlpatterns = [
    path('publish', views.publish),
    path('vote', views.vote),
    path('getIds', views.getIds),
    path('getQuestionById', views.searchQuestionById),
    path('getQuestionByLabels', views.searchQuestionByLabels),
    path('getAllClosedQuestions', views.getAllFinishedQuestions),
    path('', views.index, name='index'),
]
