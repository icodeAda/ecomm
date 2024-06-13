from django.db import models
import datetime


# categories of products
class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  

  class Meta:
     verbose_name_plural = 'categories'


#customers
class Customer(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   phone_number = models.CharField(max_length=10)
   email = models.EmailField(max_length=100)
   password = models.CharField(max_length=100)

   def __str__(self):
     return f' {self.first_name} {self.last_name}'
   

#all of our products
class Product(models.Model):
     name = models.CharField(max_length=1000)
     price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
     description = models.CharField(max_length=250, default='', blank=True,null=True)
     image = models.ImageField(upload_to='uploads/products/')
     #add sale stuff
     is_sale = models.BooleanField(default=False)
     sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

     def __str__(self):
       return self.name
     
#customers orders
class Order(models.Model):
   Product = models.ForeignKey(Product, on_delete=models.CASCADE)
   Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   address = models.CharField(max_length=100, default='', blank= True)
   Phone = models.CharField(max_length=20,  default='', blank=True)
   Date = models.DateField(default=datetime.datetime.today)
   status = models.BooleanField(default=False)

   def __str__(self):
       return self.Product
   

