# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=200)
	place=models.CharField(max_length=200)
	created_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Teacher(models.Model):
	name=models.CharField(max_length=200)
	dept=models.CharField(max_length=200)
	image=models.ImageField(upload_to ='image/')

	def __str__(self):
		return self.name

class Hod(models.Model):
	usr = models.OneToOneField(User)
	dept = models.CharField(max_length=200)

	def __str__(self):
		return self.dept

class Prince(models.Model):
	usr=models.OneToOneField(User)
	country=models.CharField(max_length=200)

	def __str__(self):
		return	self.country