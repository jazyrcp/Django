# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,View
from django.contrib.auth.models import User

from footshop.forms import ProductForm,CategoryForm,SubCategoryForm,CustomerForm
from footshop.models import Customer
# Create your views here.

class HomeView(TemplateView):
	template_name='home.html'


class ProductView(CreateView):
	template_name='newproduct.html'
	form_class= ProductForm
	success_url='product'


class CategoryView(CreateView):
	template_name='newcat.html'
	form_class=CategoryForm
	success_url='cat'


class SubCatView(CreateView):
	template_name='newsub.html'
	form_class=SubCategoryForm
	success_url='subcat'


class CustomerView(View):
	template_name='cust.html'
	form_class=CustomerForm

	def get(self,request):
		form = self.form_class()
		context = {
		'form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():

			usr = User.objects.create_user(username = request.POST.get('username'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),email=request.POST.get('email'),password=request.POST.get('pwd1'))

			cus = Customer.objects.create(
				usr = usr,
				age = request.POST.get('age'),
				gender = request.POST.get('gender'),
				place = request.POST.get('place'))
			cus.save()

			context = {
			'form':form,
			'success':'cust'
			}
			return render(request,self.template_name,context)

		else:
			form=self.form_class()
			context={
			'form':form
			}
			return render(request,self.template_name,context)


