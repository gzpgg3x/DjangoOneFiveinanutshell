# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import auth
 
class Post(models.Model):
 
  title = models.CharField(max_length=255)
 
  machine_name = models.SlugField(max_length=255, primary_key=True)
 
  content = models.TextField(blank=True)
 
  publication_date = models.DateTimeField(auto_now_add=True)
 
  def __unicode__(self):
    return self.title
 
  def excerpt(self):
    return self.content[:300] + u'…'
 
  class Meta:
    ordering = [u'-publication_date']
