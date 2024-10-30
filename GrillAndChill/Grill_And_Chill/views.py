from django.shortcuts import render, get_object_or_404 , redirect
from .models import User, Product, Order
from .forms import UserForm , ProductForm , OrderForm

def index(request):
    return render(request, 'admintemplates/index.html')  # ensure the template path is correct

# Basic Views for Users

def user_list(request):
    users = User.objects.all()
    return render(request, 'admintemplates/user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'admintemplates/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to user list after creation
    else:
        form = UserForm()
    return render(request, 'admintemplates/user_form.html', {'form': form})

def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)  # Bind form to the user instance
        if form.is_valid():
            form.save()  # Save the updated user
            return redirect('user_list')  # Redirect to the user list after successful update
    else:
        form = UserForm(instance=user)  # Populate the form with the user's current details
    
    return render(request, 'admintemplates/user_form.html', {'form': form, 'user': user})

def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if request.method == 'POST':
        user.delete()  # Delete the user
        return redirect('user_list')  # Redirect to the user list after deletion
    
    return render(request, 'admintemplates/user_confirm_delete.html', {'user': user})


# Basic Views for Products

def product_list(request):
    products = Product.objects.all()
    return render(request, 'admintemplates/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'admintemplates/product_detail.html', {'product': product})

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
            form.save()  # Save the new order
            return redirect('order_list')  # Redirect to the order list
    else:
        form = OrderForm()  # Create an empty form if GET request

    # Add Bootstrap class to all fields
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})

    return render(request, 'admintemplates/order_form.html', {'form': form})


# Update View
def order_update(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)  # Bind form to the order instance
        if form.is_valid():
            form.save()  # Save the updated order
            return redirect('order_list')  # Redirect to the order list after successful update
    else:
        form = OrderForm(instance=order)  # Populate the form with the order's current details
    
    return render(request, 'admintemplates/order_form.html', {'form': form, 'order': order})

# Delete View
def order_delete(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if request.method == 'POST':
        order.delete()  # Delete the order
        return redirect('order_list')  # Redirect to the order list after deletion
    
    return render(request, 'admintemplates/order_confirm_delete.html', {'order': order})