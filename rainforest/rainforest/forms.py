from django import forms
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.db import models
from rainforest.models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
