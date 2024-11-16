from rest_framework import serializers
from .models import User, Category, Alergen, Product, Product_Alergen, Order, Product_Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AlergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergen
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  

    class Meta:
        model = Product
        fields = '__all__'
        

class ProductAlergenSerializer(serializers.ModelSerializer):
    products_Id = ProductSerializer()  
    alergens_Id = AlergenSerializer()   

    class Meta:
        model = Product_Alergen
        fields = '__all__'

class ProductOrderSerializer(serializers.ModelSerializer):
    products_Id = ProductSerializer()  
    order_Id = OrderSerializer()        

    class Meta:
        model = Product_Order
        fields = '__all__'


class ProductAlergenDescriptionSerializer(serializers.ModelSerializer):
    alergens_Id = serializers.CharField(source='alergens_Id.description')

    class Meta:
        model = Product_Alergen
        fields = ['alergens_Id']
