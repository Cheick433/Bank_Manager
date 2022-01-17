from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import random
from .forms import VirementForm, ClientForm_Op
from .models import Op_virement
from PRopre.models import Propre
#from .forms import ClientForm_Op
from django.http import HttpResponseRedirect,HttpResponse


def ajout_virement(request):
    form1 = ClientForm_Op()
    form = VirementForm()
    if request.method == 'POST':
        form1=ClientForm_Op(request.POST)
        form = VirementForm(request.POST)
        if form.is_valid() or form1.is_valid():
            numEn = request.POST.get('num_compte')
            num_dest = request.POST.get('dest_num')
            propre1 = get_object_or_404(Propre, num_compte = numEn)
            propre2 = get_object_or_404(Propre, num_compte = num_dest)
            #tmp = propre1()
            Tr_montant=request.POST.get('montant_v')
            if propre1 is None or propre2 is None:
                return HttpResponse('Compte Nexiste pas')

            elif propre1.montant < float(Tr_montant) or propre1.montant==0.0:
                return HttpResponse('montant insiffisant or Compte Nexiste pas')
            propre1.montant = propre1.montant - float(Tr_montant)
            propre2.montant += float(Tr_montant)
            virement = Op_virement.objects.create(client=propre1, montant_v=float(Tr_montant), dest_num=num_dest)
            propre1.save()
            propre2.save()
            #tmp.delete()
            return redirect('Opvirement:ajouter_virement')
    else:
        form=VirementForm()
        form1 = ClientForm_Op()
        context = {'form':form, 'form1':form1}
        return render(request, 'virement/ajouter_virement.html', context)





