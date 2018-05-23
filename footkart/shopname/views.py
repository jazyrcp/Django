# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView

from shopname.forms import UserForm,NewProductForm
from shopname.models import Category,Product,SubCategory
# Create your views here.


class HomeView(View):
	template_name = 'home.html'

	def get(self,request):	
		return render(request,self.template_name)

class UserView(CreateView):
	template_name = 'new_user.html'
	form_class = UserForm
	success_url = 'home'

class CategoryView(ListView):
	template_name = 'category.html'
	model = Category
	context_object_name = 'data'


class SubCategoryView(View):
	template_name = 'm-casual.html'
	
	def get(self,request,catname,subname):
		cat = Category.objects.get(cat_name = catname)
		sub = SubCategory.objects.get(cat = cat, sub_name = subname)
		pro = Product.objects.filter(pro_cat = sub)
		return render(request,self.template_name,{'data':pro})


class NewProductView(View):
	template_name = 'newproduct.html'
	form_class = NewProductForm

	def get(self,request):
		form = self.form_class()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		print(request.POST)
		form = self.form_class(request.POST,request.FILES)

		if form.is_valid():
			print('hello')
			cat1 = Category.objects.get(cat_name = request.POST.get('pro_cat'))
			sub = SubCategory.objects.get(cat = cat1, sub_name = request.POST.get('pro_sub'))
			prod = Product.objects.create(
				pro_cat = sub,
				pro_name = request.POST.get('pro_name'),
				pro_brand = request.POST.get('pro_brand'),
				pro_detail = request.POST.get('pro_detail'),
				pro_color = request.POST.get('pro_color'),
				pro_price = request.POST.get('pro_price'),
				pro_image = request.FILES.get('pro_image'),
				)
			prod.save()

			# return redirect('home')
			return render(request,self.template_name,{'form':form,'success':'home'})

		else:
			form = self.form_class()
			return render(request,self.template_name,{'form':form})