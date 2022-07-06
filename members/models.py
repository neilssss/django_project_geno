from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Members(models.Model):
    first = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class Fish(models.Model):
    fish_type = models.CharField(max_length=225)
    fish_name = models.CharField(max_length=225)
    fish_size = models.CharField(max_length=225)
class Fish2(Fish):
    fish_img = models.ImageField(null=True,blank=True,upload_to="images/")
    fish_desc = models.TextField()
    available_size = models.CharField(max_length=200)
    fish_price = models.FloatField()
    available_qty = models.IntegerField(null=True,blank=True)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Fish2, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Fish2,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=250, null=False)
    lname = models.CharField(max_length=250, null=False)
    email = models.CharField(max_length=250, null=False)
    phone = models.CharField(max_length=250, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=250, null=False)
    region = models.CharField(max_length=250, null=False)
    zipcode = models.CharField(max_length=250, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=250, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    orderstatus = {
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),

    }
    status = models.CharField(max_length=150,choices=orderstatus,default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=250,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Fish2, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return'{} {}'.format(self.order.id, self.order.tracking_no)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)
    email = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=False)
    region = models.CharField(max_length=250, null=False)
    zipcode = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

