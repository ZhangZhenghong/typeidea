from django.contrib import admin
from comment import models
from .models import Comment

# Register your models here
class CommentAdmin(admin.ModelAdmin):
  list_display = ('target', 'content', 'nickname', 'website', 'created_time')
   

admin.site.register(models.Comment, CommentAdmin)
