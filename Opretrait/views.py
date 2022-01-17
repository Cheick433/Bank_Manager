from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import random
from .forms import RetraitForm, ClientForm_Op_r
from .models import Op_retrait
from PRopre.models import Propre
#from Propre.forms import ClientForm_Op
from django.http import HttpResponse


def ajout_retrait(request):
    if request.method == 'POST':
        form1=ClientForm_Op_r(request.POST)
        form = RetraitForm(request.POST)
        if form.is_valid() or form1.is_valid():
            #form.save()
            numEn = request.POST.get('num_compte')
            propre1 = get_object_or_404(Propre, num_compte = numEn)
            #tmp = propre1
            Tr_montant=request.POST.get('montant_R')
            if propre1.montant < float(Tr_montant):
                return HttpResponse('<h1>montant insiffisant<h1>')
            propre1.montant = propre1.montant - float(Tr_montant)
            retrait=Op_retrait.objects.create(client=propre1, montant_R=float(Tr_montant))
            #
            #Propre.objects.get(num_compte=numEn).montant -= Tr_montant
            propre1.save()
           # tmp.delete()
            return redirect('Opretrait:ajouter_retrait')
    else:
        messages.info(request, 'invalid')
        form=RetraitForm()
        form1 = ClientForm_Op_r()
        context = {'form':form, 'form1':form1}
        return render(request, 'retrait/ajouter_retrait.html', context)





