from django import forms
from .models import User, Product

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'password', 'gmail', 'tlf']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'ingredients', 'price', 'category', 'foto']