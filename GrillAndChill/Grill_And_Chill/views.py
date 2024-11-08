from django.contrib  import messages
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Alergen, Category, Product_Alergen, User, Product, Order , Product_Order
from django.utils import timezone
from django.db.models import Count
from datetime import timedelta
from collections import defaultdict
from .forms import UserForm , ProductForm , OrderForm, LoginForm
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
            # Obtener el correo electrónico que se está intentando crear
            email = form.cleaned_data.get('gmail')
            # Verificar si ya existe un usuario con ese correo
            if User.objects.filter(gmail=email).exists():
                messages.error(request, "Ya existe un usuario con este correo electrónico.")
            else:
                form.save()
                messages.success(request, "Usuario creado con éxito.")
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
            # Obtener el correo electrónico que se está intentando actualizar
            new_email = form.cleaned_data.get('gmail')
            # Verificar si ya existe otro usuario con ese correo, excluyendo el usuario actual
            if User.objects.filter(gmail=new_email).exclude(pk=user_id).exists():
                messages.error(request, "Ya existe un usuario con este correo electrónico.")
            else:
                form.save()  
                messages.success(request, "Usuario actualizado con éxito.")
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

def clientside_main(request):
    return render(request, 'usertemplates/base.html')


def clientside_register(request):
    if request.method == 'POST':
        erabiltzailea = User.objects.filter(gmail=request.POST.get('gmail'))
        form = UserForm(request.POST)

        if not erabiltzailea.exists():
            print("Dena ondo")
            
            print(form.data)

            if form.is_valid():
                form.save()
                return redirect('clientside_main')
        
        else:
            messages.error(request, "Ya existe un usuario con este correo.")

        
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
                    return redirect('clientside_main')
                else:
                    messages.error(request, "La contraseña es incorrecta.")
            else:
                messages.error(request, "No existe un usuario con este correo.")
        else:
            messages.error(request, "Por favor, corrija los errores del formulario.")
    else:
        form = LoginForm()

    return render(request, 'usertemplates/login.html', {'form': form})
  


class ProductAPIView(APIView):
    
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

#    def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    # def put(self, request, pk, format=None):
    #     product = self.get_object(pk)
    #     serializer = ProductSerializer(product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     product = self.get_object(pk)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
""" 
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

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class CategoryAPIViewDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class AlergenAPIViewDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Alergen.objects.get(pk=pk)
        except Alergen.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        alergen = self.get_object(pk)
        serializer = AlergenSerializer(alergen)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        alergen = self.get_object(pk)
        serializer = AlergenSerializer(alergen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        alergen = self.get_object(pk)
        alergen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
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


class ProductAlergenAPIViewDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Product_Alergen.objects.get(pk=pk)
        except Product_Alergen.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product_alergen = self.get_object(pk)
        serializer = ProductAlergenSerializer(product_alergen)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product_alergen = self.get_object(pk)
        serializer = ProductAlergenSerializer(product_alergen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_alergen = self.get_object(pk)
        product_alergen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class OrderAPIViewDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
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


class ProductOrderAPIViewDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Product_Order.objects.get(pk=pk)
        except Product_Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product_order = self.get_object(pk)
        serializer = ProductOrderSerializer(product_order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product_order = self.get_object(pk)
        serializer = ProductOrderSerializer(product_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_order = self.get_object(pk)
        product_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 """