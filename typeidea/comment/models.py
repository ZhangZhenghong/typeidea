# -*- coding: utf-8 -*-
from django.db import models
from blog.models import Post


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'delete'),
    )
    target = models.ForeignKey(Post, verbose_name="comment target")
    content = models.CharField(max_length=2000, verbose_name="content comment")
    nickname = models.CharField(max_length=50, verbose_name="nickname")
    website = models.URLField(verbose_name="website")
    email = models.EmailField(verbose_name="email")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="zhuangtai")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="creation time")

    class Meta:
        verbose_name = verbose_name_plural = "comment_ZZH"

    def __str__(self):
      return self.nickname
