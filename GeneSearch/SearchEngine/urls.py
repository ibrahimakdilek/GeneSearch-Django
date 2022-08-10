from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('citationdata/', views.CitationDataApi.as_view()),

]
