from django.db import models

# Create your models here.
class Propre(models.Model):
    num_compte = models.IntegerField(unique=True)
    montant = models.FloatField(null=True)
    Nom=models.CharField(max_length=100,null=True,default='')
    prenom=models.CharField(max_length=100,null=True,default='')
    telephone=models.CharField(max_length=12,null=True)
    date_creation=models.DateTimeField(auto_now_add=True)
    
