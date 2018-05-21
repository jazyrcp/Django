# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
GENDER = (('M','Male'),('F','Female'),('O','Others'))
SIZE=(('8','Small'),('9','Medium'),('10','Large'),('11','XLarge'))

class Customer(models.Model):
	usr = models.OneToOneField(User) 
	age = models.IntegerField()
	gender = models.CharField(max_length=3,choices=GENDER)
	place = models.CharField(max_length=200)
	created_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.usr.username

class Category(models.Model):
	cat_name=models.CharField(max_length=200)

	def __str__(self):
		return self.cat_name


class SubCategory(models.Model):
	sub_name=models.CharField(max_length=200)

	def __str__(self):
		return self.sub_name


class Product(models.Model):
	pro_cat = models.ForeignKey(SubCategory)
	pro_name =models.CharField(max_length=200)
	pro_brand =models.CharField(max_length=200)
	pro_detail = models.TextField(max_length=500)
	pro_size = models.CharField(max_length=4,choices=SIZE)
	pro_image = models.ImageField(upload_to='image/')
	pro_color =models.CharField(max_length=200)
	pro_price =models.IntegerField()

	def __str__(self):
		return self.pro_name

class Cart(models.Model):
	cust = models.ForeignKey(Customer)
	product = models.ForeignKey(Product)
	count = models.IntegerField()

	def __str__(self):
		return self.cust.usr.username


