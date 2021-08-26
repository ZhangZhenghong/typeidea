from django.contrib import admin

from .models import Category, Tag, Post

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'status', 'is_nav', 'create_time','owner')
  fields = ('name', 'status','is_nav', 'owner')
  
  def save_model(self, request, obj, form, change):
    obj.owner = request.user
    return super(CategoryAdmin, self).save_model(request, obj, form, change)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  list_display = ('name', 'status', 'create_time')
  fields = ('name', 'status')

  def save_model(self, request, obj, form, change):
    obj.owner = request.user
    return super(TagAdmin, self).save_model(request, obj, form, change)

