# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Brand(models.Model):
	name = models.CharField(max_length=200)
	

	def __str__(self):
		return self.name


class Car(models.Model):
	brand = models.ForeignKey(Brand)
	name = models.CharField(max_length=200)
	engine_cc = models.IntegerField()
	wheel_size = models.IntegerField()
	color = models.CharField(max_length=200)

	def __str__(self):
		return self.name
