from django import forms
from .models import Coustomer


class CoustomerForm(forms.ModelForm):
    class Meta:
        model = Coustomer
        fields = "__all__"
