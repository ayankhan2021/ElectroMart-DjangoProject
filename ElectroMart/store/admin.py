from django.contrib import admin
from .models import Category, Product, Customer, Cart, CartItem, Order, OrderItem, Review


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)