from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
  STATUS_NORMAL = 1
  STATUS_DELETE = 0
  STATUS_ITEMS = ( (STATUS_NORMAL, 'normal'), (STATUS_DELETE, 'delete'))
  name = models.CharField(max_length=50, verbose_name = "mingcheng")
  status = models.PositiveIntegerField(default = STATUS_NORMAL, choices = STATUS_ITEMS, verbose_name = 'zhuangtai')
  is_nav = models.BooleanField(default=False, verbose_name = 'navigation')
  owner = models.ForeignKey(User, verbose_name='author')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name = 'creation time')

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = verbose_name_plural = 'catagories'

class Tag(models.Model):
  STATUS_NORMAL = 1
  STATUS_DELETE = 0
  STATUS_ITEMS = ( (STATUS_NORMAL, 'normal'), (STATUS_DELETE, 'delete'))
  name = models.CharField(max_length=50, verbose_name = "mingcheng")
  status = models.PositiveIntegerField(default = STATUS_NORMAL, choices = STATUS_ITEMS, verbose_name = 'zhuangtai')
  is_nav = models.BooleanField(default=False, verbose_name = 'navigation')
  owner = models.ForeignKey(User, verbose_name='zuozhe')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name = 'creation time')

  class Meta:
    verbose_name = verbose_name_plural = 'Tags'
  def __str__(self):
    return self.name

class Post(models.Model):
  STATUS_NORMAL = 1
  STATUS_DELETE = 0
  STATUS_DRAFT = 2
  STATUS_ITEMS = ( (STATUS_NORMAL, 'normal'), (STATUS_DELETE, 'delete'), (STATUS_DRAFT, 'draft'))
  title = models.CharField(max_length=255, verbose_name='biaoti')
  desc = models.CharField(max_length=1024, blank=True, verbose_name = 'Zhaiyao')
  status = models.PositiveIntegerField(default = STATUS_NORMAL, choices = STATUS_ITEMS, verbose_name = 'zhuangtai')
  category = models.ForeignKey(Category, verbose_name='fenlei')
  tag = models.ManyToManyField(Tag, verbose_name = 'biaoqian')
  owner = models.ForeignKey(User, verbose_name='zuozhe')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name = 'creation time')
  
  class Meta:
    verbose_name = verbose_name_plural = 'wenzhang'
    ordering = ['-id']

  def __str__(self):
    return self.title 
  



