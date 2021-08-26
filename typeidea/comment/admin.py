from django.contrib import admin
from .models import Comment

# Register your models here
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('target', 'content', 'nickname')
  
