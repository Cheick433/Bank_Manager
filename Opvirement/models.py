from django.db import models
from PRopre.models import Propre

# Create your models here.
class Op_virement(models.Model):
    client = models.ForeignKey(Propre, null=True, on_delete=models.SET_NULL)
    montant_v = models.FloatField(null=True)
    date_virement=models.DateTimeField(auto_now_add=True)
    dest_num = models.IntegerField()

