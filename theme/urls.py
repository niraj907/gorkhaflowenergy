from django.contrib import admin
from django.urls import path
from .views import index,contact,document,view ,download_view ,  login , signup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'), 
    path('document/', document, name='document'), 
    path('view/', view, name='view'),  
    path('download/', download_view, name='download'),
    path('login/', login, name='login'), 
    path('signup/', signup, name='signup'), 
    path('', index, name='index'),
]
