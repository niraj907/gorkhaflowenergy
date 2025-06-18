from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    return render(request, 'hero.html')
def document(request):
    return render(request, 'document.html')
def view(request):
    return render(request, 'view.html')
def contact(request):
    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')


def download_view(request):
    html_content = render_to_string('view.html')
    response = HttpResponse(html_content, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="report.html"'
    return response