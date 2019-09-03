# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_photo = models.ImageField(upload_to='products/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Inquiry(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
