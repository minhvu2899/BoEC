from django import forms
from .models import Product

class FormCreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields =['title','category','price']

class UploadFileForm(forms.Form):
    file = forms.FileField()