from django.conf import settings
#from django.conf.urls import url
from . import views
from django.urls import path

app_name = "Opversement"
urlpatterns = [

  #  path('', views.index, name='index'),
    path('ajouter_versement/', views.ajout_versement, name ="ajouter_versement")

]