from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,"register.html")
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")