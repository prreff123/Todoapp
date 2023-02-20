from django import forms
from .models import Product

class TodoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price']