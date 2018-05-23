# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView,TemplateView,View,ListView,DetailView
from django.contrib.auth.models import User

from footshop.forms import ProductForm,CategoryForm,SubCategoryForm,CustomerForm
from footshop.models import Customer,Product,Cart,Category
# Create your views here.

class HomeView(View):
	template_name='home.html'

	def get(self,request):
		return render(request,self.template_name)

class ProductView(CreateView):
	template_name='newproduct.html'
	form_class= ProductForm
	success_url='product'


class CategoryView(CreateView):
	template_name='newcat.html'
	form_class=CategoryForm
	success_url='cat'




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


class ProductListView(ListView):
	template_name= 'prolist.html'
	model = Product
	context_object_name = 'data'

class ProductDetailView(DetailView):
	template_name = 'detail.html'
	model = Product
	context_object_name = 'data'

class AddCartView(View):
	def post(self,request):
		p_id =request.POST.get('product_id')
		ct = request.POST.get('count')
		u = request.user
		user = User.objects.get(username = u)
		pro = Product.objects.get(id = p_id)
		usr = Customer.objects.get(usr = user)
		cart = Cart.objects.create(cust = usr ,product = pro ,count = ct)
		cart.save()
		# return redirect('prolist')

		response = 'Success'
		return HttpResponse(json.dumps(response),content_type='json')

class CategoryListView(ListView):
	template_name = 'categories.html'
	model = Category
	context_object_name = 'data'

class MenView(ListView):
	template_name = 'men.html'
	model = SubCategory
	context_object_name = 'data'