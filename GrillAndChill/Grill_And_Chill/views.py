from django.shortcuts import render, get_object_or_404 , redirect
from .models import User, Product, Order
from .forms import UserForm , ProductForm

def index(request):
    return render(request, 'admintemplates/index.html')  # ensure the template path is correct

def user_list(request):
    users = User.objects.all()
    return render(request, 'admintemplates/user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'admintemplates/user_detail.html', {'user': user})

# Basic View for Products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'admintemplates/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'admintemplates/product_detail.html', {'product': product})

# Basic View for Orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'admintemplates/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'admintemplates/order_detail.html', {'order': order})


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to user list after creation
    else:
        form = UserForm()
    return render(request, 'admintemplates/user_form.html', {'form': form})

def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'admintemplates/user_confirm_delete.html', {'user': user})

def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list after successful update
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'admintemplates/product_form.html', {'form': form, 'product': product})

def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Redirect back to the product list after deletion
    return render(request, 'admintemplates/product_confirm_delete.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Save product to the database
            return redirect('product_list')  # Redirect to the product list
    else:
        form = ProductForm()  # Create an empty form for GET request
    
    return render(request, 'admintemplates/product_form.html', {'form': form})  # Render the form