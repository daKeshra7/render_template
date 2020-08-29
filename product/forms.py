from django import forms

from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'first_name',
            'last_name',
            'height',
            'about_you',
            'photo'           
        ]