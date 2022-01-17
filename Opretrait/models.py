from django.db import models
from PRopre.models import Propre

# Create your models here.
class Op_retrait(models.Model):
    client=models.ForeignKey(Propre, null=True, on_delete=models.SET_NULL)
    montant_R=models.FloatField(null=True)
    date_retrait=models.DateTimeField(auto_now_add=True)


