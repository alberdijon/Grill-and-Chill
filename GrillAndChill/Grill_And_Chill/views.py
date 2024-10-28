from django.shortcuts import render, get_object_or_404 , redirect
from .models import User, Product, Orders
from .forms import UserForm
# Basic View for Users
def index(request):
    return render(request, 'admintemplates/index.html')

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
    orders = Orders.objects.all()
    return render(request, 'admintemplates/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
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
