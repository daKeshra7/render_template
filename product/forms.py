from django import forms

from .models import Products

class ProductForm(forms.ModelForm):
    first_name      =  forms.CharField(label='',widget=forms.TextInput(
                        attrs={"placeholder": "First Name"}))

    last_name       =  forms.CharField(required=False, label='',widget=forms.Textarea(
                                    attrs={
                                    "placeholder": "Last name",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 10,
                                    "cols": 25}))
                                
    height          =  forms.DecimalField( initial=0.0)
    e_mail = forms.EmailField()


    class Meta:
        model = Products
        fields = [
            'first_name',
            'last_name',
            'height',
            'about_you'           
        ]
    def clean_first_name(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        if not "cfe" in first_name:
            raise forms.ValidationError("This is not a valid name")
       
        return first_name

    def clean_e_mail(self, *args, **kwargs):
        e_mail = self.cleaned_data.get('e_mail')
        if e_mail.endswith('edu'):
            raise forms.ValidationError('This is not a Valid email')
        return e_mail

# class RawProductForm(forms.Form):
#     first_name      =  forms.CharField(label='', 
#     widget=forms.TextInput(
#         attrs={
#             "placeholder": "First Name"
#         }
#         )
#     )
#     last_name       =  forms.CharField(required=False, label='',
#                             widget=forms.Textarea(
#                                 attrs={
#                                     "placeholder": "Last name",
#                                     "class": "new-class-name two",
#                                     "id": "my-id-for-textarea",
#                                     "rows": 10,
#                                     "cols": 25
#                                 }
#                             )
#     )
#     height          =  forms.DecimalField( initial=0.0)

