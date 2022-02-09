from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
#from profiles.forms import CreerUtilisateur
from django.contrib import messages


def register(request):
        #form = UserCreationForm(request.POST)
    form = CreerUtilisateur()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save() #user=form.cleaned_data.get('username')
            return redirect('signin')  # return redirect("accounts:signin")  #context = {'form': form}
    context = {'form': form}
    return render(request, 'accounts/create_account.html', context)

def sign_in(request):
    #contexte={}
    if request.method == 'POST':
        #form = AuthenticationForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) # if form.is_valid():
        if user is not None:    # user = form.get_user()
            login(request, user)  # return redirect("profiles:account_status")
            return redirect('home')
        return HttpResponse('<h1>nom ou mot de passe non valide<h1>')
    else:
        form = AuthenticationForm()
        return render(request, "accounts/sign_in.html", {'form': form})

def logout_view(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    return redirect("accounts:signin")
