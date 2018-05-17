# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
	'latest_question_list':
	}
	return HttpResponse(output)

def detail(request,question_id):
	return HttpResponse('You are lookin at question %s'%question_id)

def results(request,question_id):
	return HttpResponse('You are looking at result of %s' %question_id)

def vote(request,question_id):
	return HttpResponse('You are voting on question %s' %question_id)