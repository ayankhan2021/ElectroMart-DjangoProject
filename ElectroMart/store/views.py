from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from store.models import Product, Category, Order, OrderItem, Payment, Cart
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def userdashboard(request):
    return render(request, 'userdashboard.html')
def login(request):
    
    if request.method == 'POST':
        # handle login logic
        # if successful:
        return redirect('userdashboard')  # Redirect to user dashboard after login
    return render(request, 'login.html')
   
def categories(request):
    return render(request, 'categories.html')

def category_detail(request):
    return render(request, 'category_detail.html')
def signup(request):
    return render(request, 'signup.html')
def orders(request):
    return render(request, 'orders.html')
def logout_user(request):
    # auth_logout(request)
    # return redirect('home')
    return render(request, 'logout_user.html')
def review_dashboard(request):
    return render(request, 'review_dashboard.html')
def products(request):
    return render(request, 'products.html')
def cart_view(request):
    return render(request, 'cart.html')
def checkout(request):
    return render(request, 'checkout.html')
def tracking(request):
    return render(request, 'tracking.html')
# def product_list(request):
#     products = Product.objects.all()  # Retrieve all products
#     return render(request, 'products/product_list.html', {'products': products})

# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)  # Fetch the product by ID
#     return render(request, 'products/product_detail.html', {'product': product})


# Add to cart view
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Assuming you have a Cart model and a method to add products to it
#     cart, created = Cart.objects.get_or_create(user=request.user, active=True)  # Fetch or create a cart for the user
#     cart.products.add(product)  # Add the product to the cart
#     cart.save()
    
#     messages.success(request, f"{product.name} added to your cart!")
#     return redirect('product_list')  # Redirect to the product list page after adding

# # Remove from cart view
# def remove_from_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Fetch the cart and remove the product
#     cart = Cart.objects.get(user=request.user, active=True)
#     cart.products.remove(product)
#     cart.save()
    
#     messages.success(request, f"{product.name} removed from your cart.")
#     return redirect('cart_view')  # Redirect to the cart view page

# Order detail view
# def order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id, user=request.user)  # Get the order by ID and ensure it belongs to the user
    
#     return render(request, 'order_detail.html', {'order': order})  # Render the order detail template

# # Tracking details view
# def tracking_details(request, order_id):
#     order = get_object_or_404(Order, id=order_id, user=request.user)
    
#     # Assuming the order model has tracking details
#     tracking_info = order.tracking_info  # Assuming `tracking_info` is a field in the `Order` model
    
#     return render(request, 'tracking_details.html', {'order': order, 'tracking_info': tracking_info})

@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)




