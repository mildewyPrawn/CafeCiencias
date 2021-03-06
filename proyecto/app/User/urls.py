from . import views
from .views import *
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.urls import path

"""
Todas las urls en User
"""

app_name = 'User'
urlpatterns = [
    #path('accounts/', include('django.contrib.auth.urls')),
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    #TODAS LAS SIGUIENTES DIRECCIONES VIENEN CON LA DE ARRIBA
    #accounts/login/ [name='login']
    #accounts/logout/ [name='logout']
    #accounts/password_change/ [name='password_change']
    #accounts/password_change/done/ [name='password_change_done']
    #accounts/password_reset/ [name='password_reset']
    #accounts/password_reset/done/ [name='password_reset_done']
    #accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    #accounts/reset/done/ [name='password_reset_complete']
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    path("error505",error505, name="error505"),
    path('',Index, name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('admin/', admin.site.urls),
    # TODO: Cambiar eventos := comidas
    path('eventos/',views.EventosN.as_view(), name='eventos'),
    path('eventos/all',EventosList, name='eventosList'),
    path('eventos/home',Eventos, name='eventosHome'),
    path('eventos/home.html',Eventos, name='eventosHome'),
    path('eventos/index.html/',Eventos, name='eventos'),
    path('eventos/index/',Eventos, name='eventos'),
    path('home/', views.HomeView.as_view(),name='home'),
    path('home/',Index, name='index'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('login/register.html/', views.Register, name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register2'),
    path('register/Organizador/', views.RegistroOrganizador.as_view(),
         name='registroOrg'),
    path('register/cambioContrasena/', views.CambioContrasena.as_view(),
         name='cambio'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^organizador_registrado/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.organizador_registrado, name='organizador_registrado'),
    url(r'^register/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activateEvent, name='activateEvent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
