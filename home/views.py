from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "homebase.html")

def index2(request):
    return render(request, "homebase2.html")

def contact(request):
    return render(request, "contact.html")

def contact2(request):
    return render(request, "contact2.html")

def blog(request):
    return render(request, "blog.html")

def blog3(request):
    return render(request, "blog2.html")

def about(request):
    return render(request, "about.html")

def about2(request):
    return render(request, "about2.html")

def cart(request):
    return render(request, "cart.html")

def cart2(request):
    return render(request, "cart2.html")

def elements(request):
    return render(request, "elements.html")

def checkout(request):
    return render(request, "checkout.html")

def checkout2(request):
    return render(request, "checkout2.html")

def confirmation(request):
    return render(request, "confirmation.html")

def shop(request):
    return render(request, "shop.html")

def shop2(request):
    return render(request, "shop2.html")

def blog2(request):
    return render(request, "blog-details.html")

def blog4(request):
    return render(request, "blog-details2.html")

def login_form(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('./index2.html')
        
        else:
            return render(request, "login.html")
    
    else:
        return render(request, "login.html")

def logout(request):
    return redirect('/index.html')

def join_form(request):
    if request.method=="POST":
        username=request.POST["username"]
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request, "./signup.html", 
                {
                    "eror":"username kullanılıyor", 
                    "username":username,
                    "email":email,
                    "first_name":first_name,
                    "last_name":last_name
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "./signup.html", 
                {
                    "eror":"username kullanılıyor", 
                    "username":username,
                    "email":email,
                    "first_name":first_name,
                    "last_name":last_name
                })
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,
                    password=password)
                    user.save()
                    return redirect("./login.html")
        else:
            return render(request, "./signup.html", 
            {
                "eror":"parola eşleşmiyor",
                "username":username,
                "email":email,
                "first_name":first_name,
                "last_name":last_name
            })
    return render(request, "./signup.html")

def shopping_bag(request):
    return render(request, "shopping-bag.html")

def product_details(request):
    return render(request, "product_details.html")

def product_details2(request):
    return render(request, "product_details2.html")