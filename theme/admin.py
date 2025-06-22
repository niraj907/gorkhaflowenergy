from django.contrib import admin
from .models import *

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    readonly_fields = ('name', 'email', 'submitted_at', 'message','contact_Number')


admin.site.register(Document)


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title',)
    list_filter = ('published_date',)
    ordering = ('-published_date',)

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PhotoInline]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)

@admin.register(HomepageNews)
class HomepageNewsAdmin(admin.ModelAdmin):
    list_display = ('message', 'date')
    ordering = ('-date',)
    search_fields = ('message',)