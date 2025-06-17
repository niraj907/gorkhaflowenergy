from django.contrib import admin
from django.urls import path
from .views import index,contact, login , signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'), 
    path('login/', login, name='login'), 
    path('signup/', signup, name='signup'), 
    path('', index, name='index'),
]
