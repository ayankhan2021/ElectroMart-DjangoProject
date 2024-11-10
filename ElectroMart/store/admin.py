from django.contrib import admin
from .models import Category, Product, Customer, Cart, CartItem, Order, OrderItem, Review


# Register Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# Register Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')

# Register Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'postal_code')
    search_fields = ('user__username', 'address', 'city')

# Register Cart model
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_at')
    search_fields = ('customer__user__username',)

# Register CartItem model
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_filter = ('cart',)

# Register Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_amount', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__user__username',)

# Register OrderItem model
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_filter = ('order',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'rating', 'created_at')
    list_filter = ('product', 'rating')
    search_fields = ('customer__user__username', 'product__name')
