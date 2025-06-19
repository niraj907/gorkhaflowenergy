from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'), 
    path('documents/', views.documents_view, name='documents'), 
    path('document/view/', view, name='view'),  
    path('news/', news, name='news'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('login/', login, name='login'), 
    path('signup/', signup, name='signup'), 
    path('', index, name='index'),
]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)