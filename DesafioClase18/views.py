from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Familiares

def familiaresForm (request): 
    if request.method == "POST": # separo el dato que viene del form
        formulario = FamiliaresForm(request.POST)
        if formulario.is_valid: 
            print(formulario) # ¿funciona el cleaned_data sin el print?
            familiar_info = formulario.cleaned_data 
            nombre = familiar_info["nombre"] # separe cada variable porque sino era muy largo la generación del objeto
            apellido = familiar_info["apellido"]
            fecha_nac = familiar_info["fecha_nac"]
            dni = familiar_info["DNI"] 
            familiar = Familiares(nombre=nombre,apellido=apellido,fecha_nac=fecha_nac,DNI=dni)
            familiar.save() 
                        # nombre = familiar_info["nombre"]
            familiares = Familiares.objects.all() # aprovecho y al mismo le renderizo el contexto
            contexto = {"familiares":familiares}
            return render (request,"Familiar.html",contexto) #lo mando al html.
    else:

        miformu = FamiliaresForm()

        return render (request,"FamiliaresForm.html",{"miformu":miformu})
    
def loginv(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            usuario = datos["username"]
            contra = datos["password"]
            user = authenticate(username=usuario, password=contra)

            if user:
                login(request, user)
                return render(request,"Familiar.html", {"mensaje": f"Bienvenido {usuario}"})
            
            else:
                return render(request,"Familiar.html", {"mensaje": f"Datos Incorrectos"})

        else:
            return render(request,"Familiar.html", {"mensaje": f"Datos Incorrectos"})

    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form":form})

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.cleaned_data["username"]      
            form.save()
            return render(request, "Familiar.html", {"mensaje": f"Usuario creado"})  
            
    else:
        form = UserCreationForm()
        return render(request, "register.html", {"form":form})
