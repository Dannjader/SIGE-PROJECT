from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from dispositivos.models import Dispositivo, Servicio
from .forms import CustomUserCreationForm
from dispositivos.models import CustomUser

# # Create your views here.


def inicio(request):
    return render(request, 'index.html')


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            CustomUser = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, CustomUser)
            messages.success(request, 'Se resgistro correctamente')
        data['form'] = form
    return render(request, './registration/register.html', data)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dispositivos')
    else:
        form = AuthenticationForm()
    return render(request, './registration/login.html', {'form': form})


def dispositivos_list(request):
    dispositivos = Dispositivo.objects.all()
    return render(request, 'dispositivos_list.html', {'dispositivos': dispositivos})


def servicios_list(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios_list.html', {'servicios': servicios})
