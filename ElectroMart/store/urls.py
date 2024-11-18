from django.urls import path
from . import views
from .views import product_list_api


urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('userdashboard', views.userdashboard,name='userdashboard'),
    path('userDashboard/orders',views.orders,name='my_orders'),
    path('logout/', views.logout, name='logout'),
    path('userDashboard/reviews',views.review_dashboard , name='reviews'),    
    # path('products/', views.product_list, name='product_list'),  # Updated path for listing all products
    # path('products/<int:product_id>/', views.product_detail, name='product_detail'), #single product
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('cart/', views.cart_view, name='cart_view'),
    # path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),    
    # path('checkout/', views.checkout, name='checkout'),
    # path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    # path('logout/', views.logout_user, name='logout'),
    # path('tracking/<int:order_id>/', views.tracking_details, name='tracking_details'),
    path('products/', product_list_api, name='product_list_api')
]