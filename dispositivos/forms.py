from django import forms
<<<<<<< HEAD
from dispositivos.models import Servicio
=======
from .models import Tecnico, Servicio

# creating a form


class InputForm(forms.Form):

    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(
        help_text="Enter 6 digit roll number"
    )
    password = forms.CharField(widget=forms.PasswordInput())


class TecnicoForm(forms.ModelForm):

    class Meta:
        model = Tecnico()
        fields = '__all__'

>>>>>>> stayling

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = '__all__'
