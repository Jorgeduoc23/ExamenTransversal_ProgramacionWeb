from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('mascota/', views.mascota,name='mascota'),
    path('contacto/', views.contacto,name='contacto'),
    path('pag_perros/', views.pag_perros,name='pag_perros'),
    path('pag_gatos/', views.pag_gatos,name='pag_gatos'),
    path('agregar-mascota/', views.agregarmascota,name='agregar'),

    #path perros
    path('Fichas_perros/Abby', views.Abby,name='Fichas_perros/Abby'),
    path('Fichas_perros/Almendra', views.Almendra,name='Fichas_perros/Almendra'),
    path('Fichas_perros/Bito', views.Bito,name='Fichas_perros/Bito'),
    path('Fichas_perros/Celeste', views.Celeste,name='Fichas_perros/Celeste'),
    path('Fichas_perros/Firulais', views.Firulais,name='Fichas_perros/Firulais'),
    path('Fichas_perros/Pedro', views.Pedro,name='Fichas_perros/Pedro'),




    #path gatos

    path('Fichas_gatos/Alice', views.Alice,name='Fichas_gatos/Alice'),
    path('Fichas_gatos/Kiki', views.Kiki,name='Fichas_gatos/Kiki'),
    path('Fichas_gatos/Leo', views.Leo,name='Fichas_gatos/Leo'),
    path('Fichas_gatos/Milo', views.Milo,name='Fichas_gatos/Milo'),
    path('Fichas_gatos/Oliver', views.Oliver,name='Fichas_gatos/Oliver'),
    path('Fichas_gatos/Romeo', views.Romeo,name='Fichas_gatos/Romeo'),
]