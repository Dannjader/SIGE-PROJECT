from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from dispositivos.models import Servicio

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','cargo']


class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = '__all__'
