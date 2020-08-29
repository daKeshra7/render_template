from django import forms
from .models import product_info

class product_info_form(forms.ModelForm):
    class Meta:
        model = product_info
        fields = {
            'name',
            'description',
            'price',
            'comment'
        }
