from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
  STATUS_NORMAL = 1
  STATUS_DELETE = 0
  STATUS_ITEMS = ( (STATUS_NORMAL, 'normal'), (STATUS_DELETE, 'delete'))
  title = models.CharField(max_length=255, verbose_name='biaoti')
  href = models.URLField(verbose_name='lianjie')
  status = models.PositiveIntegerField(default = STATUS_NORMAL, choices = STATUS_ITEMS, verbose_name = 'zhuangtai')
  weight = models.PositiveIntegerField(default= 1, choices = zip(range(1,6), range(1,6)), verbose_name = 'quanzhong', help_text = 'quanzhong he shunxu')
  owner = models.ForeignKey(User, verbose_name='zuozhe')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name='creation time')
  
  class Meta:
    verbose_name = verbose_name_plural = 'you lian'
    
class SideBar(models.Model):
  STATUS_SHOW = 1
  STATUS_HIDE = 0
  STATUS_ITEMS = ( (STATUS_SHOW, 'zhanshi'), (STATUS_HIDE, 'Hidden'))
  SIDE_TYPE = ((1, 'html'), (2, 'latest'), (3, 'hottest'), (4, 'recent'))
  title = models.CharField(max_length=255, verbose_name='biaoti')
  display_type = models.PositiveIntegerField(default=1, choices = SIDE_TYPE, verbose_name='zhanshi leixing')
  content = models.CharField(max_length=500, blank=True, verbose_name='neirong', help_text = 'if setting is not html, empty')
  status = models.PositiveIntegerField(default=STATUS_SHOW, choices = STATUS_ITEMS, verbose_name='Zhuangtai')
  owner = models.ForeignKey(User, verbose_name='zuozhe')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name='creation time')

  class Meta:
    verbose_name = verbose_name_plural = 'ce bian lan'
    
