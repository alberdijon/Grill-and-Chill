from django.urls import path, include
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('administrador/', views.index, name='index'),  
    path('administrador/users/', views.user_list, name='user_list'),
    path('administrador/users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('administrador/users/<int:user_id>/update/', views.user_update, name='user_update'),  
    path('administrador/users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('administrador/users/create/', views.user_create, name='user_create'),
    
    path('administrador/products/', views.product_list, name='product_list'),
    path('administrador/products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('administrador/products/<int:product_id>/update/', views.product_update, name='product_update'),
    path('administrador/products/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('administrador/products/create/', views.product_create, name='product_create'),
    
    
<<<<<<< Updated upstream
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/update/', views.order_update, name='order_update'),  
    path('orders/<int:order_id>/delete/', views.order_delete, name='order_delete'),
    
    
    path('orders/revenue/', views.monthly_revenue, name='monthly_revenue'),

    path('clientside/', views.clientside_index, name='clientside_main'),
    path('clientside/register/', views.clientside_register, name='clientside_register'),
    path('clientside/log-in/', views.clientside_login, name='clientside_login'),
  
    path('clientside/index/', views.clientside_index, name='clientside_index'),
    path('clientside/produktuak/', views.clientside_produktuak, name='clientside_produktuak'),
    path('clientside/saskia/', views.clientside_saskia, name='clientside_saskia'),
    path('clientside/kontaktuak/', views.clientside_kontaktuak, name='clientside_kontaktuak'),
=======
    path('administrador/orders/', views.order_list, name='order_list'),
    path('administrador/orders/create/', views.order_create, name='order_create'),
    path('administrador/orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('administrador/orders/<int:order_id>/update/', views.order_update, name='order_update'),

    path('administrador/orders/<int:order_id>/delete/', views.order_delete, name='order_delete'),    
    path('administrador/orders/revenue/', views.monthly_revenue, name='monthly_revenue'),
  
  
  
    path('', views.clientside_index, name='clientside_main'),

    path('register/', views.clientside_register, name='clientside_register'),
    path('log-in/', views.clientside_login, name='clientside_login'),
    path('perfil/', views.clientside_perfil, name='clientside_perfil'),
    path('logout/', views.clientside_logout, name='clientside_logout'),

    path('produktuak/', views.clientside_produktuak, name='clientside_produktuak'),
  
  
    path('kontaktuak/', views.clientside_kontaktuak, name='clientside_kontaktuak'),
>>>>>>> Stashed changes

  
  
    # path('v1/users/', views.UserAPIView.as_view()),
    # path('v1/users/<int:pk>/', views.UserAPIViewDetail.as_view()),
    # path('v1/categories/', views.CategoryAPIView.as_view()),
    # path('v1/categories/<int:pk>/', views.CategoryAPIViewDetail.as_view()),
    # path('v1/alergens/', views.AlergenAPIView.as_view()), 
    # path('v1/alergens/<int:pk>/', views.AlergenAPIViewDetail.as_view()),
  

<<<<<<< Updated upstream
  
    

    path('v1/products/', views.ProductAPIView.as_view()),
    path('v1/products/<int:pk>/', views.ProductAPIViewDetail.as_view()),
    
   
    # path('v1/users/', views.UserAPIView.as_view()),
    # path('v1/users/<int:pk>/', views.UserAPIViewDetail.as_view()),
    # path('v1/categories/', views.CategoryAPIView.as_view()),
    # path('v1/categories/<int:pk>/', views.CategoryAPIViewDetail.as_view()),
    # path('v1/alergens/', views.AlergenAPIView.as_view()), 
    # path('v1/alergens/<int:pk>/', views.AlergenAPIViewDetail.as_view()),
    # path('v1/product_alergens/', views.ProductAlergenAPIView.as_view()),
    # path('v1/product_alergens/<int:pk>/', views.ProductAlergenAPIViewDetail.as_view()),
    # path('v1/orders/', views.OrderAPIView.as_view()),
    # path('v1/orders/<int:pk>/', views.OrderAPIViewDetail.as_view()),
    # path('v1/product_orders/', views.ProductOrderAPIView.as_view()),
    # path('v1/product_orders/<int:pk>/', views.ProductOrderAPIViewDetail.as_view()),

    
]
   
=======
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),

    path('v1/products/', views.ProductAPIView.as_view()),
    path('v1/products/<int:pk>/', views.ProductAPIViewDetail.as_view()),


    path('v1/product_alergens/', views.ProductAlergenAPIView.as_view()),
    path('v1/product_alergens/<int:pk>/', views.ProductAlergenAPIViewDetail.as_view()),
 
    path('v1/users/<int:pk>/', views.UserAPIViewDetail.as_view()),


    path('api/cart/<int:user_id>/', views.UserCartAPIView.as_view(), name='user_cart'),
    
    path('api/update_cart/', views.update_cart, name='update_cart'),
    
    path('api/cart/<int:user_id>/product/<int:product_id>/delete/', views.DeleteProductFromCartAPIView.as_view(), name='delete_cart_product'),

    
]
>>>>>>> Stashed changes
