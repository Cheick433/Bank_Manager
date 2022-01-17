from django.conf import settings
#from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = "Opretrait"
urlpatterns = [

  #  path('', views.index, name='index'),
    path('ajouter_retrait/', views.ajout_retrait, name='ajouter_retrait')

]