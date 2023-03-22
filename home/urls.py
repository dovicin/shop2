from django import http, views
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.index, name='index'),
    path("index.html", views.index, name='index.html'),
    path("homebase.html", views.index, name='homebase.html'),
    path("index2.html", views.index2, name='index2.html'),
    path("elements.html", views.elements, name='elements.html'),
    path("homebase2.html", views.index2, name='homebase2.html'),
    path("contact.html", views.contact, name='contact.html'),
    path("contact2.html", views.contact2, name='contact2.html'),
    path("blog.html", views.blog, name='blog.html'),
    path("blog2.html", views.blog3, name='blog2.html'),
    path("about.html", views.about, name='about.html'),
    path("about2.html", views.about2, name='about2.html'),
    path("cart.html", views.cart, name='cart.html'),
    path("cart2.html", views.cart2, name='cart2.html'),
    path("login", views.login_form, name='login.html'),
    path("logout.html", views.logout, name='logout.html'),
    path("signup", views.join_form, name='signup.html'),
    path("signup.html", views.join_form, name='signup.html'),
    path("login.html", views.login_form, name='login.html'),
    path("shopping-bag.html", views.shopping_bag, name='shopping-bag.html'),
    path("blog-details.html", views.blog2, name='blog-details.html'),
    path("blog-details2.html", views.blog4, name='blog-details2.html'),
    path("product_details.html", views.product_details, name='product_details.html'),
    path("product_details2.html", views.product_details2, name='product_details2.html'),
    path("checkout.html", views.checkout, name='checkout.html'),
    path("checkout2.html", views.checkout2, name='checkout2.html'),
    path("confirmation.html", views.confirmation, name='confirmation.html'),    
    path("shop.html", views.shop, name='shop.html'),
    path("shop2.html", views.shop2, name='shop2.html'),
]