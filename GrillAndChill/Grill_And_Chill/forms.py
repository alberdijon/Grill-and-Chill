from django import forms
from .models import User, Product , Order

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'password', 'gmail', 'tlf', 'direction']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'ingredients', 'price', 'category', 'foto']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_Id', 'price', 'ordered', 'direction']