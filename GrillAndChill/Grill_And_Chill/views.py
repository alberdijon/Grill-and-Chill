from django.shortcuts import render, get_object_or_404 , redirect
from .models import User, Product, Order
from django.utils import timezone
from datetime import timedelta
from .forms import UserForm , ProductForm , OrderForm

def index(request):
    one_month_ago = timezone.now() - timedelta(days=30)
    orders = Order.objects.filter(order_Date__gte=one_month_ago)

    total_revenue = sum(order.price for order in orders)
    order_count = orders.count()
   
    chart_data = [['Order Date', 'Revenue']] 

    for order in orders:
        chart_data.append([order.order_Date.strftime('%Y-%m-%d'), order.price])

    return render(request, 'admintemplates/monthly_revenue.html', {
        'total_revenue': total_revenue,
        'order_count': order_count,
        'chart_data': chart_data
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


