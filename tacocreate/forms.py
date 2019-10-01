from django import forms
from .models import Taco


class TacoForm(forms.ModelForm):
    class Meta:
        model = Taco
        fields = ["shell_choice","base_layer_choice","mixin_choice","condiment_choice","seasoning_choice"]