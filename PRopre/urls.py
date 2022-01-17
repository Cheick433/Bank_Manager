from django.urls import path
from . import views
from . import forms

urlpatterns = [

    path('', views.home, name="home"),
    path('client',views.ajouter_client,name="ajouter_client"),
    path('client/<str:pk>', views.info_client, name="info_client"),
    path('modifier/<str:pk>',views.modiffier_client,name="modiffier_client"),
    path('supprimer/<str:pk>',views.supprimer_client,name="supprimer_client"),
]
