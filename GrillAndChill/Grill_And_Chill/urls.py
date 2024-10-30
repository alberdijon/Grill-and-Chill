from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('products/<int:product_id>/update/', views.product_update, name='product_update'),
    path('products/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('products/create/', views.product_create, name='product_create'),
]