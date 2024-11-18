from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.contrib.auth import login as django_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from store.models import Product, Category, Order, OrderItem, Payment, Cart, CartItem



# Create your views here.

User = get_user_model()

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


@login_required
def userdashboard(request):
    # user = request.user
    # orders = Order.objects.filter(user=user).order_by('-order_date')  # Fetch orders for the logged-in user
    if request.user.is_authenticated:
        return render(request, 'userdashboard.html')
    
    return redirect('login')  # Redirect to login page if user is not authenticated


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            django_login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')  # Replace 'home' with your home page URL name
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')


# Signup view
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please use a different email address.")
        else:
            # Create user and authenticate
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(username=username, password=password)  # Authenticate user
            if user is not None:
                django_login(request, user)  # Log the user in
                messages.success(request, "Signup successful! Welcome!")
                return redirect('home')  # Redirect to home page

    return render(request, 'signup.html')


# Logout view (optional)
def logout_view(request):
    print("Logout view called")  # Debugging line
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

def categories(request):
    return render(request, "categories.html")

def category_detail(request):
    return render(request, "category_detail.html")

def orders(request):
    return render(request, "orders.html")

def review_dashboard(request):
    return render(request, "review_dashboard.html")

def products(request):
    return render(request, "products.html")

def cart_view(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def tracking(request):
    return render(request, "tracking.html")


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


def product_list_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
