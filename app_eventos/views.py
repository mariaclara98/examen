from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Evento, Participante
from .forms import EventoForm, CustomUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

def home_view(request):
    return render(request, 'base.html')

def exit(request):
    logout(request)
    return redirect('base.html')

class RegisterView(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm


def evento_list(request):
    eventos = Evento.objects.all()
    return render(request, 'secciones/evento_list.html', {'eventos': eventos})


@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.creador = request.user
            evento.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'secciones/evento_create.html', {'form': form})

@login_required
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'secciones/evento_list.html', {'eventos': eventos})

@login_required
def inscribirse_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if not Participante.objects.filter(usuario=request.user, evento=evento).exists():
        Participante.objects.create(usuario=request.user, evento=evento)
        return redirect('ver_mis_inscripciones')
    return render(request, 'secciones/error_inscripcion.html', {'evento': evento})

@login_required
def ver_mis_inscripciones(request):
    inscripciones = Participante.objects.filter(usuario=request.user)
    return render(request, 'secciones/ver_mis_inscripciones.html', {'inscripciones': inscripciones})

@login_required
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, creador=request.user)
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'secciones/evento_update.html', {'form': form})

@login_required
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, creador=request.user)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'secciones/evento_confirm_delete.html', {'evento': evento})
