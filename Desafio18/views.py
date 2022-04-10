from django.shortcuts import render
from .forms import FamiliaresForm
from .models import Familiares

# Create your views here.
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
            contexto = {"familiares":familiares, "nombre":nombre}
            return render (request,"Familiar.html",contexto) #lo mando al html.
    else:

        miformu = FamiliaresForm()

        return render (request,"FamiliarForm.html",{"miformu":miformu})
    