from django import forms

class FamiliaresForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    fecha_nac = forms.DateField()
    DNI = forms.IntegerField ()