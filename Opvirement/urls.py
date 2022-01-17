from django.conf import settings
#from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = "Opvirement"
urlpatterns = [

  #  path('', views.index, name='index'),
    path('ajouter_virement/', views.ajout_virement, name="ajouter_virement")

]