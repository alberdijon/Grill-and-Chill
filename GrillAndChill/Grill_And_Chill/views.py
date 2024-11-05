from django.shortcuts import render, get_object_or_404 , redirect
from .models import Alergen, Category, Product_Alergen, User, Product, Order , Product_Order
from django.utils import timezone
from django.db.models import Count
from datetime import timedelta
from collections import defaultdict
from .forms import UserForm , ProductForm , OrderForm
from .serializers import UserSerializer, CategorySerializer, AlergenSerializer, ProductSerializer, ProductAlergenSerializer, OrderSerializer, ProductOrderSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
def monthly_revenue(request):
    # Your logic for the view goes here.
    return render(request, 'admintemplates/monthly_revenue.html', context={})

def index(request):
    one_month_ago = timezone.now() - timedelta(days=30)
    orders = Order.objects.filter(order_Date__gte=one_month_ago).order_by('order_Date')

    # Agrupar ingresos por fecha
    revenue_by_date = defaultdict(float)
    for order in orders:
        revenue_by_date[order.order_Date] += order.price  

    chart_data = [['Order Date', 'Revenue']]
    for date, total_price in revenue_by_date.items():
        chart_data.append([date.strftime('%Y-%m-%d'), total_price])

    # Obtener los 5 productos más vendidos
    top_products = Product_Order.objects.values('products_Id__name')\
                     .annotate(total=Count('products_Id'))\
                     .order_by('-total')[:5]

    product_chart_data = [['Product', 'Units Sold']]
    for product in top_products:
        product_chart_data.append([product['products_Id__name'], product['total']])

    # Obtener los 5 clientes con más pedidos
    top_customers = Order.objects.values('user_Id__name')\
                     .annotate(total=Count('user_Id'))\
                     .order_by('-total')[:5]

    customer_chart_data = [['Customer', 'Orders']]
    for customer in top_customers:
        customer_chart_data.append([customer['user_Id__name'], customer['total']])

    total_revenue = sum(revenue_by_date.values())
    order_count = len(orders)

    return render(request, 'admintemplates/monthly_revenue.html', {
        'total_revenue': total_revenue,
        'order_count': order_count,
        'chart_data': chart_data,
        'product_chart_data': product_chart_data,
        'customer_chart_data': customer_chart_data
    })
# Basic Views for Users

#List view
def user_list(request):
    users = User.objects.all()
    return render(request, 'admintemplates/user_list.html', {'users': users})

#Detail view
def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'admintemplates/user_detail.html', {'user': user})

# Create View
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  
    else:
        form = UserForm()
    return render(request, 'admintemplates/user_form.html', {'form': form})

# Update View
def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user) 
        if form.is_valid():
            form.save()  
            return redirect('user_list') 
    else:
        form = UserForm(instance=user)  
    
    return render(request, 'admintemplates/user_form.html', {'form': form, 'user': user})

# Delete View
def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if request.method == 'POST':
        user.delete()  
        return redirect('user_list')  
    
    return render(request, 'admintemplates/user_confirm_delete.html', {'user': user})


# Basic Views for Products

# List View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'admintemplates/product_list.html', {'products': products})

# Detail View
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'admintemplates/product_detail.html', {'product': product})

# Upadate product
def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'admintemplates/product_form.html', {'form': form, 'product': product})
# Delete product
def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  
    return render(request, 'admintemplates/product_confirm_delete.html', {'product': product})

# Create product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('product_list') 
    else:
        form = ProductForm()  
    
    return render(request, 'admintemplates/product_form.html', {'form': form})  
# Basic Views for Orders

# List View
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'admintemplates/order_list.html', {'orders': orders})

# Detail View
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'admintemplates/order_detail.html', {'order': order})

# Create View
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('order_list')  
    else:
        form = OrderForm()  

   
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})

    return render(request, 'admintemplates/order_form.html', {'form': form})


# Update View
def order_update(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order) 
        if form.is_valid():
            form.save()  
            return redirect('order_list')  
    else:
        form = OrderForm(instance=order) 
    
    return render(request, 'admintemplates/order_form.html', {'form': form, 'order': order})

# Delete View
def order_delete(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if request.method == 'POST':
        order.delete()  
        return redirect('order_list')  
    
    return render(request, 'admintemplates/order_confirm_delete.html', {'order': order})


class UserAPIView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryAPIView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlergenAPIView(APIView):
    def get(self, request, format=None):
        alergens = Alergen.objects.all()
        serializer = AlergenSerializer(alergens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlergenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductAlergenAPIView(APIView):
    def get(self, request, format=None):
        product_alergens = Product_Alergen.objects.all()
        serializer = ProductAlergenSerializer(product_alergens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductAlergenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderAPIView(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductOrderAPIView(APIView):
    def get(self, request, format=None):
        product_orders = Product_Order.objects.all()
        serializer = ProductOrderSerializer(product_orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)