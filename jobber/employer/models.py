# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employer(models.Model):

	e_firm = models.CharField(max_length=50)
	e_user = models.OneToOneField(User,related_name='employers')
	e_detail = models.TextField(max_length=5000)
	e_place = models.CharField(max_length=50)
	e_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.e_user.username


class Category(models.Model):
	c_name = models.CharField(max_length=200)

	def __str__(self):
		return self.c_name


class SubCategory(models.Model):
	s_cat = models.ForeignKey(Category,related_name='subcategories')
	s_name = models.CharField(max_length=200)

	def __str__(self):
		return self.s_name


class Job(models.Model):

	j_employer = models.ForeignKey(Employer,related_name='jobs')
	j_name = models.CharField(max_length=50)
	j_subcat = models.ForeignKey(SubCategory,related_name='jobs')
	j_detail = models.TextField(max_length=5000)
	j_requirement = models.TextField(max_length=5000)
	j_created = models.DateTimeField(auto_now=True)
	j_salary = models.IntegerField(null=True)

	def __str__(self):
		return self.j_name
