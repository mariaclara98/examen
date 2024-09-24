from django.contrib.auth.models import User
from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_evento = models.DateField()
    lugar = models.CharField(max_length=255)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Participante(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['usuario', 'evento']  # Restringe inscripción duplicada

    def __str__(self):
        return f'{self.usuario.username} inscrito en {self.evento.nombre}'
