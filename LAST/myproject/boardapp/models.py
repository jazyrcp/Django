# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
	name=models.CharField(max_length=200,unique=True)
	description=models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Topic(models.Model):
	subject=models.CharField(max_length=30)
	last_updated=models.DateTimeField(auto_now_add=True)
	board =models.ForeignKey(Board,related_name='topics')
	starter=models.ForeignKey(User,related_name='topics')

	def __str__(self):
		return self.subject


class Post(models.Model):
	message=models.TextField(max_length=3000)
	topic=models.ForeignKey(Topic,related_name='posts')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(null=True)
	created_by=models.ForeignKey(User,related_name='posts')
	updated_by=models.ForeignKey(User,null=True,related_name='+')

	