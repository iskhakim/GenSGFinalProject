from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def cart_view(request):
    return render(request, 'cart.html')

def about_view(request):
    return render(request, 'about.html')