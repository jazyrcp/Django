# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView,ListView,View,TemplateView
from app1.forms import FirstForm,SecondForm,ThirdForm	
from app1.models import Second,First,Third
# Create your views here.


class HomeView(TemplateView):
	template_name = 'index.html'


class FirstView(CreateView):
	template_name='app1/app1_create.html'
	form_class = FirstForm
	success_url = '/first'

class SecondView(CreateView):
	template_name='app1/app1_create.html'
	form_class = SecondForm
	success_url = '/second'

class SecondListView(ListView):
	template_name='app1/app1_view.html'
	model=Second

class FirstListView(ListView):
	template_name='app1/app1_view.html'
	model=First

class ThirdView(View):
	template_name='app1/app1_third.html'
	form_class  =ThirdForm

	def get(self,request):
		form = self.form_class()
		context = {
		'form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			context = {
			'form':form,
			'success':"saved Succesfully"
			}
			return render(request,self.template_name,context)
		else:
			context={
			'form':form
			}	
			return render(request,self.template_name,context)
# class SecondListView(View):
# 	template_name='app1/app1_view.html'

# 	def get(self,request):
# 		sec_obj = Second.objects.all()
# 		context={
# 		'data':sec_obj
# 		}
# 		return render(request,self.template_name,context)
		

