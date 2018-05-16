# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
	name=models.CharField(max_length=200)
	place=models.CharField(max_length=200)
	ph=models.IntegerField()


	def __str__(self):
		return self.name

	class Meta():
		ordering=['name']

class Customer(models.Model):
	employee=models.OneToOneField(Employee)
	name=models.CharField(max_length=200)
	place=models.CharField(max_length=200)
	ph=models.IntegerField()

	def __str__(self):
		return self.name

	class Meta():
		ordering=['name']

class Sample(models.Model):
	name=models.CharField(max_length=200)
	place=models.CharField(max_length=200)
	email=models.EmailField()
	create_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name