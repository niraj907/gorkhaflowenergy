from django.shortcuts import render

def index(request):
    return render(request, 'hero.html')
def contact(request):
    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')