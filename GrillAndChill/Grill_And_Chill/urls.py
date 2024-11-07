from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/update/', views.user_update, name='user_update'),  
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('users/create/', views.user_create, name='user_create'),
    
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<int:product_id>/update/', views.product_update, name='product_update'),
    path('products/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('products/create/', views.product_create, name='product_create'),
    
    
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/update/', views.order_update, name='order_update'),  
    path('orders/<int:order_id>/delete/', views.order_delete, name='order_delete'),
    
    
    path('orders/revenue/', views.monthly_revenue, name='monthly_revenue'),

    path('clientside/', views.clientside_main, name='clientside_main'),
    path('clientside/register/', views.clientside_register, name='clientside_register'),
    path('clientside/index/', views.clientside_index, name='clientside_index'),
    path('clientside/produktuak/', views.clientside_produktuak, name='clientside_produktuak'),
    path('clientside/saskia/', views.clientside_saskia, name='clientside_saskia'),
    path('clientside/kontaktuak/', views.clientside_kontaktuak, name='clientside_kontaktuak'),
  
    path('v1/users/', views.UserAPIView.as_view()),
    path('v1/users/<int:pk>/', views.UserAPIViewDetail.as_view()),
    path('v1/categories/', views.CategoryAPIView.as_view()),
    path('v1/categories/<int:pk>/', views.CategoryAPIViewDetail.as_view()),
    path('v1/alergens/', views.AlergenAPIView.as_view()), 
    path('v1/alergens/<int:pk>/', views.AlergenAPIViewDetail.as_view()),
    path('v1/products/', views.ProductAPIView.as_view()),
    path('v1/products/<int:pk>/', views.ProductAPIViewDetail.as_view()),
    path('v1/product_alergens/', views.ProductAlergenAPIView.as_view()),
    path('v1/product_alergens/<int:pk>/', views.ProductAlergenAPIViewDetail.as_view()),
    path('v1/orders/', views.OrderAPIView.as_view()),
    path('v1/orders/<int:pk>/', views.OrderAPIViewDetail.as_view()),
    path('v1/product_orders/', views.ProductOrderAPIView.as_view()),
    path('v1/product_orders/<int:pk>/', views.ProductOrderAPIViewDetail.as_view()),


]
