from django.http import HttpResponse
from django.shortcuts import render

from .models import Familiares
from .forms import FamiliaresForm

def familiaresForm (request):
    if request.method == "POST":
        formulario = FamiliaresForm(request.POST)
        if formulario.is_valid:
            print(formulario)
            familiar_info = formulario.cleaned_data
            nombre = familiar_info["nombre"]
            apellido = familiar_info["apellido"]
            fecha_nac = familiar_info["fecha_nac"]
            dni = familiar_info["DNI"]
            familiar = Familiares(nombre=nombre,apellido=apellido,fecha_nac=fecha_nac,DNI=dni)
            familiar.save()
                        # nombre = familiar_info["nombre"]
            familiares = Familiares.objects.all()
            contexto = {"familiares":familiares}
            return render (request,"Familiar.html",contexto)
    else:

        miformu = FamiliaresForm()

        return render (request,"FamiliaresForm.html",{"miformu":miformu})
    
