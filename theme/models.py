from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime
import os
import shutil
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import FileSystemStorage
from django.urls import reverse


class ContactMessage(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_Number = PhoneNumberField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"


class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title