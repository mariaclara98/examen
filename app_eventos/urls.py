from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_evento, name='crear_evento'),
    path('', views.listar_eventos, name='listar_eventos'),
    path('logout/', exit ,name="exit"), 
    path('inscribirse/<int:evento_id>/', views.inscribirse_evento, name='inscribirse_evento'),
    path('mis-inscripciones/', views.ver_mis_inscripciones, name='ver_mis_inscripciones'),
    path('editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
]
