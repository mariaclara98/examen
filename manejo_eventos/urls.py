from django.contrib import admin 
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app_eventos.views import RegisterView, CustomLoginView, home_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', include('app_eventos.urls')),
    path('', home_view, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),  
]
