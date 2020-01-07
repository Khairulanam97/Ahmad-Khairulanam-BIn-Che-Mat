from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'medicine_ID', 'category', 'supplier', 'unit_price', 'quantity', 'Date_in', 'description')
