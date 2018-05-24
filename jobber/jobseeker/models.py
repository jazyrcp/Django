# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from employer.models import Job,Employer
# Create your models here.


class Seeker(models.Model):

	s_user = models.OneToOneField(User)
	s_qualification = models.CharField(max_length=200)
	s_experience = models.CharField(max_length=200)
	s_ph = models.IntegerField()
	s_resume = models.FileField(upload_to='media/resume/',null=True)
	s_image = models.ImageField(upload_to='media/image/',null=True)
	s_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.s_user.username


class Application(models.Model):

	a_job = models.ForeignKey(Job,related_name='applications')
	a_seeker = models.ForeignKey(Seeker,related_name='applications')
	a_cover = models.CharField(max_length=1000)
	a_resume = models.FileField(upload_to='media/resume/')
	a_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.a_job.j_name


class Review(models.Model):

	r_firm = models.ForeignKey(Employer,related_name='reviews')
	r_seeker = models.ForeignKey(Seeker,related_name='reviews')
	r_detail = models.CharField(max_length=5000)
	r_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.r_firm.e_firm