from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from users.models import client

# Create your views here.

def connectas(request):
    return render(request, 'connectas.html')

def connectasclient(request):
    if request.method == 'POST':
        formulaire = LoginForm(request.POST)
        if formulaire.is_valid(request):
            pseudo = formulaire.cleaned_data['pseudo']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            data = authenticate(request, username=pseudo,
                                password=mot_de_passe)
            if data is not None:
                login(request, data)

                clientp = client.objects.get(pseudo=pseudo)
                # project = myProject.objects.get(clientp=clientp)
                
            return redirect('client_project',pseudo)
        # We pass the form to the template even if it is not valid
        return render(request, 'login_as_client.html', {'form': formulaire})
    # We pass the form to the template for GET requests
    return render(request, 'login_as_client.html', {'form': LoginForm()})

def connectassupervisor(request):
    if request.method == 'POST':
        formulaire = LoginForm(request.POST)
        if formulaire.is_valid(request):
            pseudo = formulaire.cleaned_data['pseudo']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            data = authenticate(request, username=pseudo,password=mot_de_passe)
            if data is not None:
                login(request, data)
                #### on va redirect dashboard #####
                # return redirect('map/')
            return redirect('display',pseudo)
        # We pass the form to the template even if it is not valid
        return render(request, 'login.html', {'form': formulaire})
    # We pass the form to the template for GET requests
    return render(request, 'login.html', {'form': LoginForm()})

def compte(request, pk, variable=None, pseudo=None):
    if pk == 'supervisor':
        if request.method == 'POST':
            formulaire = Form_supervisor(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'supervisor'
                #######PB here
                return redirect('add_client',pseudo)
                # return redirect('map', variable, pseudo)
            return render(request, 'signup.html', {'form': formulaire})
        return render(request, 'signup.html', {'form': Form_supervisor()})
    else:
        if request.method == 'POST':
            formulaire = Form_client(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'client'
                ####### redirect dashboard normally
                #return redirect('map/',variable, pseudo)
                return redirect('interface_c')
            return render(request, 'signup.html', {'form': formulaire})
        return render(request, 'signup.html', {'form': Form_client()})
       