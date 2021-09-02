from django.contrib import admin
from .models import Category, Tag, Post
from blog import models
from django.utils.html import format_html
from django.urls import reverse
from .adminforms import PostAdminForms
from typeidea.custom_site import custom_site

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'status', 'is_nav', 'create_time','owner','post_count')
  fields = ('name', 'status','is_nav', 'owner')
  search_fields=('name',)
  list_editale=('owner',)
  
  def save_model(self, request, obj, form, change):
    obj.owner = request.user
    return super(CategoryAdmin, self).save_model(request, obj, form, change)
  
  def post_count(self, obj):
    return obj.post_set.count()

  def __str__(self):
    return self.name
 
  post_count.short_description = 'wenzhang count'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  list_display = ('name', 'status', 'create_time')
  fields = ('name', 'status')
  def __str__(self):
    return self.name

  def save_model(self, request, obj, form, change):
    obj.owner = request.user
    return super(TagAdmin, self).save_model(request, obj, form, change)

class CategoryOwnerFilter(admin.SimpleListFilter):
  title = 'list filter'
  parameter_name = 'owner_category'

  def lookups(self, request, model_admin):
    return Category.objects.filter(owner=request.user).value_list('id', 'name')

  def queryset(self, request, queryset):
    category_id = self.value()
    if category_id:
      return queryset.filter(category_id=self.value)
    else:
      return queryset

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  form = PostAdminForms
  list_display = ('title', 'desc', 'status', 'category', 'owner', 'create_time',  'operator')
  list_display_links =[]

  list_filter = ['category']
  search_fiels = ['title', 'category__name']

  actions_on_top = True
  actions_on_bottom = True
  
  save_on_top = True

  fieldsets = (
                ('basic setting', {
                                   'description':'baisic setting desc','fields':(('title', 'category'), 'status')
                                   }
                 ),
                ('content',{
                             'fields':('desc',)
                           }
                ),
                ('extra info',{
                               'classes':('collapse',),
                               'fields':('tag',)
                               }

                )
                
              )

#  fields = (('category','title'), 'desc', 'status', 'tag')

  def __str__(self):
    return self.name

  def operator(self, obj):
    return format_html(
      '<a href = "{}"> edit </a>',
      reverse('admin:blog_post_change', args=(obj.id,))
     )
  operator.short_description = 'operate'

  def save_model(self, request, obj, form, change):
    obj.owner = request.user
    return super(PostAdmin, self).save_model(request,obj,form,change)

#admin.site.register(models.Category, CategoryAdmin, site=custom_site)
#admin.site.register(models.Tag, TagAdmin)
#admin.site.register(models.Post, PostAdmin)

