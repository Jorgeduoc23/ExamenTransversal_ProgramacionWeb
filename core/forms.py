from django import forms
from .models import Macota


class MascotaForm(forms.ModelForm):
    class Meta:
        model=Macota
        fields='__all__'
