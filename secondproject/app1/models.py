# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class First(models.Model):
	name=models.CharField(max_length=200)
	place=models.CharField(max_length=200)
	image=models.ImageField(upload_to='image/')

	def __str__(self):
		return self.name

class Second(models.Model):
	name=models.CharField(max_length=200)
	place=models.CharField(max_length=200)
	image=models.ImageField(upload_to='image/')

	def __str__(self):
		return self.name

class Third(models.Model):
	name=models.CharField(max_length=200)
	place=models.CharField(max_length=200)

	def __str__(self):
		return self.name