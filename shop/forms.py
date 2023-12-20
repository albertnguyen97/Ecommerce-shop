from django import forms
from .models import Product
from django.utils.text import slugify
import requests
from django.core.files.base import ContentFile


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'quantity_product', 'image', 'description', 'price', 'address',
                  'available']
        labels = {
            'name': 'Product Name',
            'image': 'Product Image',
            'description': 'Product description',
            'price': 'Product Price',
            'available': 'Available',
        }
        prepopulated_fields = {'slug': ('name'.lower(),)}

    def save(self, commit=True):
        product = super().save(commit=False)
        product.slug = slugify(product.name)  # Set the slug based on the name

        if product.quantity_product == 0:
            product.available = False

        if commit:
            product.save()

        return product


class ProductDeleteForm(forms.Form):
    class Meta:
        model = Product
        fields = ['name']
        labels = {
            'name': 'Product Name',
        }
        prepopulated_fields = {'slug': ('name'.lower(),)}
    confirmation = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="I confirm that I want to delete this product."
    )