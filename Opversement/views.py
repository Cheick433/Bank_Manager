from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import random
from .forms import VersementForm, ClientForm_Op_v
from .models import Op_versement
from PRopre.models import Propre
#from Propre.forms import ClientForm_Op


def ajout_versement(request):
    if request.method == 'POST':
        form1 = ClientForm_Op_v(request.POST)
        form = VersementForm(request.POST)
        if form.is_valid() or form1.is_valid():
            # form.save()
            numEn = request.POST.get('num_compte')
            propre1 = get_object_or_404(Propre, num_compte = numEn)
            # tmp = propre1
            Tr_montant = request.POST.get('montant_vr')
            propre1.montant  += float(Tr_montant)
            versement = Op_versement.objects.create(client=propre1, montant_vr=float(Tr_montant))
            #
            # Propre.objects.get(num_compte=numEn).montant -= Tr_montant
            propre1.save()
            messages.success(request, 'Ton operation est fait par succes')
            # tmp.delete()
            return redirect('Opversement:ajouter_versement')
    else:

        form=VersementForm()
        form1 = ClientForm_Op_v()
        context = {'form':form, 'form1':form1}
        return render(request, 'versement/ajouter_versement.html', context,)





