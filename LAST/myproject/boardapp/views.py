# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from boardapp.models import Board
# Create your views here.

def home(request):
	boards=Board.objects.all()
	return render(request,'home.html',{'boards':boards})

def board_topics(request,pk):
	board=Board.objects.get(pk=pk)
	return render(request,'topics.html',{'board':board})