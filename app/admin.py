from django.contrib import admin
from .models import Blog,Contact,Comment
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'auther', 'is_published', 'created_at')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'is_solved', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')



admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
