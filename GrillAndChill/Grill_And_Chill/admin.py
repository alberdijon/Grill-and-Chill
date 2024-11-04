from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Alergen)
admin.site.register(Product_Alergen)
admin.site.register(Product_Order)
admin.site.register(Order)
admin.site.register(Category)