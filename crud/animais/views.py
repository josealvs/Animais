from itertools import product
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from django.shortcuts import HttpResponse, render, redirect
from .models import Cidade, Estado, Resgate, Denuncia
from .forms import DenunciaForm, ResgateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django


# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username = username).first()
        if user:
            return HttpResponse('esse nome de usuario ja esta em uso')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect('login')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user) 
            return redirect ('index')
        else:
            return HttpResponse('email ou senha invalidos')

def list_resgates(request):
    if request.user.is_authenticated:

        resgates = Resgate.objects.filter(usuario=request.user)
        return render(request, 'resgates.html', {'resgates': resgates})
    return redirect('login')
    
def list_denuncias(request):
    if request.user.is_authenticated:
        denuncias = Denuncia.objects.filter(usuario=request.user)
        return render(request, 'denuncias.html', {'denuncias': denuncias})
    return redirect('login')

def create_resgates(request):
    if request.user.is_authenticated:
        estados = Estado.objects.all()
        cidades = Cidade.objects.all()

        form = ResgateForm(request.POST or None)
        if form.is_valid():
            form.instance.usuario = request.user
            form.save()
            return redirect ('list_resgates')
        
        return render(request, 'resgates-form.html', {'form': form, 'estados' : estados, 'cidades': cidades})
    return redirect('login')

def create_denuncias(request):
    if request.user.is_authenticated:
        form = DenunciaForm(request.POST or None)

        if form.is_valid():
            form.instance.usuario = request.user
            form.save()
            return redirect ('list_denuncias')

        return render(request, 'denuncias-form.html', {'form': form})
    return redirect('login')

def update_resgates(request, codResgate):
    if request.user.is_authenticated:
        resgate = Resgate.objects.get(codResgate = codResgate)
        form = ResgateForm(request.POST or None, instance = resgate)

        if form.is_valid():
            form.save()
            return redirect('list_resgates')

        return render(request, 'resgate.html', {'form': form, 'resgate': resgate})
    return redirect('login')

def update_denuncias(request, codDenuncia):
    if request.user.is_authenticated:
        denuncia = Denuncia.objects.get(codDenuncia = codDenuncia)
        form = DenunciaForm(request.POST or None, instance = denuncia)

        if form.is_valid():
            form.save()
            return redirect('list_denuncias')

        return render(request, 'denuncia.html', {'form': form, 'denuncia': denuncia})
    return redirect('login')

def delete_resgates(request, codResgate):

    if request.user.is_authenticated:
        resgate = Resgate.objects.get(codResgate = codResgate)

        if request.method == 'POST':
            resgate.delete()
            return redirect('list_resgates')

        return render(request, 'res-delete-confirm.html', {'resgate': resgate})
    return redirect('login')


def delete_denuncias(request, codDenuncia):
    if request.user.is_authenticated:
        denuncia = Denuncia.objects.get(codDenuncia = codDenuncia)

        if request.method == 'POST':
            denuncia.delete()
            return redirect('list_denuncias')

        return render(request, 'den-delete-confirm.html', {'denuncia': denuncia})
    return redirect('login')

def sobre(request):
    return render(request, 'sobre.html')


def index(request):

    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect ('login')
