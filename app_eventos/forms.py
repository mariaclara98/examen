from django import forms
from .models import Evento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha_evento', 'lugar', 'imagen']

    # Validación para fechas futuras
    def clean_fecha_evento(self):
        fecha = self.cleaned_data.get('fecha_evento')
        if fecha < timezone.now().date():
            raise forms.ValidationError('La fecha del evento debe ser en el futuro.')
        return fecha

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

