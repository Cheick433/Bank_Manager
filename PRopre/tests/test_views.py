from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Propre
from .forms import ClientForm
from Opvirement.models import Op_virement
from Opversement.models import Op_versement
from Opretrait.models import Op_retrait
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import ClientModelForm


#def index(request):
   # return HttpResponse("Hello, world. You're at the polls index.")
def home(request):
    return render(request, 'client/index.html')
# Create your views here.
def ajouter_client(request):
    form=ClientForm()
    clients = Propre.objects.all()
    if request.method == 'POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            nom = request.POST.get('Nom')
            Prenom = request.POST.get('prenom')
            num = request.POST.get('num_compte')
            tel = request.POST.get('telephone')
            client = Propre.objects.create(num_compte=num, montant=0.0, Nom=nom, prenom=Prenom, telephone=tel)
            #form.save()
            return redirect('ajouter_client')
    context={'form':form,'clients':clients}
    return render(request, 'client/list_client.html', context)

def info_client(request, pk):
    client1 = Propre.objects.get(id=pk)
    virements = Op_virement.objects.filter(client = client1)
    versements = Op_versement.objects.filter(client = client1)
    retraits = Op_retrait.objects.filter(client = client1)
    context = {'client1':client1,'virements':virements, 'versements':versements,'retraits':retraits}
    return render(request, 'client/info_client.html', context)


def modiffier_client(request, pk):
    clients=Propre.objects.get(id = pk)
    form1=ClientModelForm(instance=clients)
    if request.method == 'POST':
         if form1.is_valid():
            #form.save()
            nom=request.POST.get('Nom')
            Prenom = request.POST.get('prenom')
            num=request.POST.get('num_compte')
            Montant=clients.montant
            tel=request.POST.get('telephone')
            #clients.delete()
            client=Propre.objects.create(id=pk, num_compte=num, montant=float(Montant), Nom=nom, prenom=Prenom, telephone=tel)
            setattr(client,'montant','Montant')
            return redirect('modiffier_client')
            #clients.delete()
    clients.delete()
    context={'form1':form1,'client':clients}
    #return render(request, 'client/modiffier.html', context)
    return render(request, 'client/modiffier_client.html', context)
    
 
def supprimer_client(request, pk):
    client=Propre.objects.get(id = pk)
    if request.method == 'POST':
        client.delete()
        return redirect('supprimer_client')
    return redirect('supprimer_client')
    #return HttpResponse(request, 'nest pas suppromer')
    #context={'item':client}
    #return render(request, 'client/list_client_2.html', context)

def list_client(request):
    clients=Propre.objects.all()
    context={'clients':clients}
    return render(request, 'client/list_client_2.html', context)


