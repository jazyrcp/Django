# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
	cat_name=models.CharField(max_length=200)

	def __str__(self):
		return self.cat_name


class SubCategory(models.Model):
	cat = models.ForeignKey(Category,related_name = 'subcategories')
	sub_name = models.CharField(max_length=200)

	def __str__(self):
		return self.sub_name


class Product(models.Model):
	pro_cat = models.ForeignKey(SubCategory,related_name = 'products')
	pro_name =models.CharField(max_length=200)
	pro_brand =models.CharField(max_length=200)
	pro_detail = models.TextField(max_length=500)
	pro_image = models.ImageField(upload_to='image/')
	pro_color =models.CharField(max_length=200)
	pro_price =models.IntegerField()

	def __str__(self):
		return self.pro_name

class Cart(models.Model):
	cust = models.ForeignKey(User,related_name = 'carts')
	product = models.ForeignKey(Product,related_name = 'carts')
	count = models.IntegerField()

	def __str__(self):
		return self.cust.usr.username
