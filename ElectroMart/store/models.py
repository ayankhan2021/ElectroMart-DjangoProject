from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart {self.id} for {self.customer}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='Processing')

    def __str__(self):
        return f'Order {self.id} by {self.customer}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} of {self.product.name} in order {self.order.id}'
    

class Review(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)  # Rating out of 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.customer.user.username} on {self.product.name}'


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    payment_number = models.IntegerField()
    payment_menthod = models.CharField(max_length=50)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

# class Payment(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     payment_method = models.CharField(max_length=20, choices=[
#         ('Credit Card', 'Credit Card'),
#         ('Debit Card', 'Debit Card'),
#         ('PayPal', 'PayPal'),
#         ('Bank Transfer', 'Bank Transfer')
#     ])
#     payment_date = models.DateTimeField(auto_now_add=True)
#     payment_status = models.CharField(max_length=20, choices=[
#         ('Pending', 'Pending'),
#         ('Completed', 'Completed'),
#         ('Failed', 'Failed'),
#         ('Refunded', 'Refunded')
#     ])
#     transaction_id = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return f"Payment {self.transaction_id} for Order {self.order.id}"


# class Address(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE ,related_name='addresses')
#     address_type = models.CharField(max_length=10, choices=[
#         ('Billing', 'Billing'),
#         ('Shipping', 'Shipping')
#     ])
#     address_line1 = models.CharField(max_length=255)
#     address_line2 = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=20)
#     country = models.CharField(max_length=100)
    
#     def __str__(self):
#         return f"{self.address_type} Address for {self.customer.name}"

class TrackingDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # One order can have many tracking details
    courier_name = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered')
    ])
    current_location = models.CharField(max_length=255, null=True, blank=True)  # Optional field for location updates
    estimated_delivery = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tracking Update for Order {self.order.id} - {self.tracking_number}"
    

    