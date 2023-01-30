from django.shortcuts import render
from .models import Macota
from .forms import MascotaForm

# Create your views here.


def home(request):
    mascotas =Macota.objects.all()
    data={
        'mascotas':mascotas
    }

    return render(request, "core/home.html" , data)
    


def mascota(request):
    return render(request, "core/mascota.html")
    
    
def contacto(request):
    return render(request, "core/contacto.html")


def pag_perros(request):
    return render(request, "core/pag_perros.html")


def pag_gatos(request):
    return render(request, "core/pag_gatos.html")


#vistas perros

def Abby(request):
    return render(request, "core/Fichas_perros/Abby.html")


def Almendra(request):
    return render(request, "core/Fichas_perros/Almendra.html")


def Bito(request):
    return render(request, "core/Fichas_perros/Bito.html")
    
    
def Celeste(request):
    return render(request, "core/Fichas_perros/Celeste.html")


def Firulais(request):
    return render(request, "core/Fichas_perros/Firulais.html")


def Pedro(request):
    return render(request, "core/Fichas_perros/Pedro.html")






#vistas gatos

def Alice(request):
    return render(request, "core/Fichas_gatos/Alice.html")


def Kiki(request):
    return render(request, "core/Fichas_gatos/Kiki.html")


def Leo(request):
    return render(request, "core/Fichas_gatos/Leo.html")
    
    
def Milo(request):
    return render(request, "core/Fichas_gatos/Milo.html")


def Oliver(request):
    return render(request, "core/Fichas_gatos/Oliver.html")


def Romeo(request):
    return render(request, "core/Fichas_gatos/Romeo.html")



def agregarmascota(request):
    data={
        'form': MascotaForm()
    }
    if request.method =='POST':
        formulario=MascotaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
                data["form"] = formulario
    return render(request, 'core/mascotas/agregar.html',data)

