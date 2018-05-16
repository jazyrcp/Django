# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,View

from appfour.forms import BrandForm,CarForm,BigForm
from appfour.models import Car,Brand
# Create your views here.


class HomeView(TemplateView):
	template_name = 'home.html'

class BrandView(CreateView):
	template_name = 'brand.html'
	form_class = BrandForm
	success_url = 'success'

class CarView(CreateView):
	template_name = 'car.html'
	form_class = CarForm
	success_url = 'success'


class BigView(View):
	template_name = 'big.html'
	form_class = BigForm

	def get(self,request):
		form = self.form_class()
		context = {
		'form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			brnd = Brand.objects.create(name=request.POST.get('brand_name'))
			brnd.save()
			carr = Car.objects.create(brand=brnd,name = request.POST.get('car_name')
				,engine_cc=request.POST.get('engine'),wheel_size=request.POST.get('wheel_size'),color=request.POST.get('color'))
			carr.save()
			context = {
			'form':form,
			'success':'saved Succedfully'
			}
		return render(request,self.template_name,context)

