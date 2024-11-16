from django.contrib  import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404 , redirect
import logging
from .models import User, Product, Order , Product_Order, Product_Alergen
from django.utils import timezone
from django.db.models import Count
from datetime import timedelta
from collections import defaultdict
from .forms import UserForm , ProductForm , OrderForm, LoginForm
from .serializers import ProductAlergenDescriptionSerializer, UserSerializer,  ProductSerializer, ProductAlergenSerializer, ProductOrderSerializer

from django.http import Http404, JsonResponse
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
# Create User
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('gmail')
            if User.objects.filter(gmail=email).exists():
                messages.error(request, "A user with this email already exists.")
            else:
                user = form.save(commit=False)  
                user.password = make_password(form.cleaned_data['password'])  
                user.save() 
                messages.success(request, "User created successfully.")
                return redirect('user_list')
    else:
        form = UserForm()
    
    return render(request, 'admintemplates/user_form.html', {'form': form})

# Update User
def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)   
        if form.is_valid():
            new_email = form.cleaned_data.get('gmail')    
            if User.objects.filter(gmail=new_email).exclude(pk=user_id).exists():
                messages.error(request, "A user with this email already exists.")
            else:
                user = form.save(commit=False) 
                user.password = make_password(form.cleaned_data['password'])  
                user.save() 
                messages.success(request, "User updated successfully.")
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
            new_name = form.cleaned_data.get('name')
        if Product.objects.filter(name=new_name).exclude(pk=product_id).exists():
                messages.error(request, "Ya existe un producto con este nombre.")
        else:
                form.save()
                messages.success(request, "Producto actualizado con éxito.")
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

        # Primero valida el formulario
        if form.is_valid():
            # Verificar si hay un producto con el mismo nombre solo después de validar el formulario
            if Product.objects.filter(name=form.cleaned_data.get('name')).exists():
                messages.error(request, "Ya existe un producto con este nombre.")
            else:
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


#Client side
  
def clientside_index(request):
    return render(request, 'usertemplates/index.html')

def clientside_produktuak(request):
    return render(request, 'usertemplates/produktuak.html')

def clientside_kontaktuak(request):
    return render(request, 'usertemplates/kontaktuak.html')


def clientside_register(request):
    if request.method == 'POST':
        existing_user = User.objects.filter(gmail=request.POST.get('gmail'))
        form = UserForm(request.POST)

        if not existing_user.exists():
            print("All good")
            print(form.data)

            if form.is_valid():
              
                user = form.save(commit=False)
                
               
                user.password = make_password(form.cleaned_data['password'])
                user.is_active = False  

                user.save()
                return render(request, 'usertemplates/register.html', {
                    'form': form,
                    'success': 'Your account has been successfully created.' 
                })
            else:
                return render(request, 'usertemplates/register.html', {
                    'form': form,
                    'error': 'Unable to create your account. Please check the form.'  
                })


        else:
            messages.error(request, "A user with this email already exists.")
            
    else:
        form = UserForm()

    return render(request, 'usertemplates/register.html', {'form': form})
  


def clientside_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            gmail = form.cleaned_data['gmail']
            password = form.cleaned_data['password']
            
            usuario = User.objects.filter(gmail=gmail).first()

            if usuario:
                if password == usuario.password:
                    request.session['user_id'] = usuario.id 
                    return redirect('clientside_main')
                else:
                    messages.error(request, "La contraseña es incorrecta.")
            else:
                messages.error(request, "No existe un usuario con este correo.")
        else:
            messages.error(request, "Por favor, corrija los errores del formulario.")
    else:
        form = LoginForm()

    return render(request, 'usertemplates/logIn.html', {'form': form})

def clientside_logout(request):
    logout(request)
    return redirect('clientside_main')

def add_to_cart(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))

        if not product_id:
            print("Error: Product ID is empty or not received.")
            return redirect('clientside_produktuak')
        else:
            print(f"Product ID received: {product_id}")

        product = Product.objects.get(id=product_id)
        user = User.objects.get(id=user_id)

        price = product.price * quantity
        direccion = user.direction


        try:
            order = Order.objects.get(user_Id=user, ended=False)

            order.price += price
            order.ordered += quantity  # Sumar la cantidad de productos
            order.save()  # Guardamos los cambios en la orden existente

            for _ in range(quantity):
                product_order = Product_Order(
                    products_Id=product,
                    order_Id=order  # Asignamos la orden existente
                )
                product_order.save()

            print("Producto añadido a la orden existente.")
        except Order.DoesNotExist:
            # Si no existe una orden abierta, creamos una nueva
            print("Creando nueva orden.")
            order = Order(
                user_Id=user,
                price=price,
                ordered="0",
                direction=direccion,
                ended=False 
            )
            order.save() 

            for _ in range(quantity):
                product_order = Product_Order(
                    products_Id=product,
                    order_Id=order 
                )
                product_order.save()

        return redirect('clientside_produktuak')

    return redirect('clientside_produktuak')

def clientside_perfil(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('clientside_login')
    
    user = get_object_or_404(User, id=user_id)
    return render(request, 'usertemplates/Perfil.html', {'user': user})


class ProductAPIView(APIView):
    
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

class ProductAPIViewDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    


class ProductAlergenAPIViewDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Product_Alergen.objects.get(pk=pk)
        except Product_Alergen.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            product_alergens = Product_Alergen.objects.filter(products_Id=pk)
            
            if not product_alergens:
                return Response({"detail": "No allergens found for this product."}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = ProductAlergenDescriptionSerializer(product_alergens, many=True)
            return Response([item['alergens_Id'] for item in serializer.data])

class UserAPIViewDetail(APIView):
    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserCartAPIView(APIView):
    
    def get(self, request, user_id, format=None):
        try:
            # Obtener la orden activa del usuario
            order = Order.objects.get(user_Id_id=user_id, ended=False)
        except Order.DoesNotExist:
            return Response({"detail": "No active order found for this user."}, status=404)

        # Obtener los productos de esa orden
        product_orders = Product_Order.objects.filter(order_Id=order)
        serializer = ProductOrderSerializer(product_orders, many=True)
        return Response({"order": order.id, "price": order.price, "products": serializer.data})