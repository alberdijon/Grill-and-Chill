from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    surname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gmail = models.EmailField(max_length=100)
    tlf = models.IntegerField()

    def __str__(self):
        return f"{self.name} -- {self.surname} -- {self.password} -- {self.gmail} -- {self.tlf}"


class Alergen(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} -- {self.description}"
  

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=1000)
    price = models.FloatField(max_length=6)
    foto = models.TextField()

    def __str__(self):
        return f"{self.id} -- {self.name} -- {self.description} -- {self.ingredients} -- {self.alergens} -- {self.price} -- {self.foto}"
    

class Product_Alergen(models.Model):
    code = models.AutoField(primary_key=True)
    products_Id  = models.ForeignKey(Product, on_delete=models.CASCADE)
    alergens_Id  = models.ForeignKey(Alergen, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} -- {self.products_Id} -- {self.alergens_Id}"


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    products_Id  = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    order_Date = models.TimeField(auto_now=True)
    ordered = models.FloatField()

    def __str__(self):
        return f"{self.id} -- {self.user_Id} -- {self.products_Id} -- {self.price} -- {self.order_Date} -- {self.ordered}"

