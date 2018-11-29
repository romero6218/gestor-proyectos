from django import forms
from . import models

class Form_proyecto(forms.ModelForm):
    class Meta:
        model= models.Proyecto
        fields= ("nombre", "descripcion", "numero_usuarios", "duracion", "ubicacion", "categoria")
