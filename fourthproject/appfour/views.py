# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib
import urllib2
import json
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,View,ListView,DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth,messages
from django.conf import settings
from django.shortcuts import redirect
from appfour.forms import BrandForm,CarForm,BigForm,UserForm,BikeForm
from appfour.models import Car,Brand,Bike

from django.contrib.auth.decorators import user_passes_test

# Create your views here.


class HomeView(View):
	template_name = 'home.html'

	def get(self,request):
		usr = request.user
		user_obj = User.objects.get(username=usr.username)
		context = {
		'data':user_obj
		}
		return render(request,self.template_name,context)


class DeleteUser(View):
	def get(self,request):
		usr = request.user
		user_obj = User.objects.get(id=usr.id).delete()
		return redirect("login")

class DeleteUserS(View):
	def get(self,request,uid):
		if request.user.is_superuser:
			user_obj = User.objects.get(id=uid).delete()
			return redirect("userlist")
		else:
			return redirect('login')
class EditUser(View):
	template_name = 'user.html'
	form_class = UserForm

	def get(self,request):
		usr = request.user
		form = UserForm(
			initial={
			'first_name': usr.first_name,
			'last_name': usr.last_name,
			'email':usr.email,
			'username':usr.username,
			})
		context= {
		'form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		usr = request.user
		editer = User.objects.get(id=usr.id)
		if form.is_valid():
			
			editer.first_name=request.POST.get('first_name')
			editer.last_name=request.POST.get('last_name')
			editer.last_name=request.POST.get('last_name') 
			editer.username=request.POST.get('username')
			editer.email=request.POST.get('email')
			editer.save()
			
			return redirect('home')

		else:
			context = {
			'form':form
			}
		return render(request,self.template_name,context)
		
class EditUserS(View):
	template_name = 'user.html'
	form_class = UserForm

	def get(self,request,uid):
		if request.user.is_superuser:
			usr = User.objects.get(id=uid)
			form = UserForm(
				initial={
				'first_name': usr.first_name,
				'last_name': usr.last_name,
				'email':usr.email,
				'username':usr.username,
				})
			context= {
			'form':form
			}
			return render(request,self.template_name,context)
		else:
			return redirect('login')


	def post(self,request,uid):
		form = self.form_class(request.POST)
		
		editer = User.objects.get(id=uid)
		if form.is_valid():

			editer.first_name=request.POST.get('first_name')
			editer.last_name=request.POST.get('last_name')
			editer.last_name=request.POST.get('last_name') 
			editer.username=request.POST.get('username')
			editer.email=request.POST.get('email')
			editer.save()
			
			return redirect('userlist')

		else:
			context = {
			'form':form
			}
		return render(request,self.template_name,context)


class UserListView(ListView):
	template_name='userlist.html'
	model = User


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

			''' Begin reCAPTCHA validation '''
			recaptcha_response = request.POST.get('g-recaptcha-response')
			url = 'https://www.google.com/recaptcha/api/siteverify'
			values = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
			}
			data = urllib.urlencode(values)
			req = urllib2.Request(url, data)
			response = urllib2.urlopen(req)
			result = json.load(response)
			''' End reCAPTCHA validation '''

			if result['success']:
				brnd = Brand.objects.create(name=request.POST.get('brand_name'))
				brnd.save()
				carr = Car.objects.create(brand=brnd,name = request.POST.get('car_name')
					,engine_cc=request.POST.get('engine'),wheel_size=request.POST.get('wheel_size'),color=request.POST.get('color'))
				carr.save()
				context = {
				'form':form,
				'success':'saved Succedfully'
				}
				messages.success(request, 'success!')
			else:
				messages.error(request, 'Invalid reCAPTCHA. Please try again.')
			
		return render(request,self.template_name,context)

class UserView(CreateView):
	template_name = 'user.html'
	form_class = UserForm
	success_url = 'success'


def login(request):
	form = AuthenticationForm()
	if request.user.is_authenticated():
		if request.user.is_superuser:
			return redirect('/userlist/')
		else:
			return redirect('/home/')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			# correct username and password login the user
			auth.login(request, user)
			if request.user.is_superuser:
				return redirect("/userlist/")# or your url name
			else:
				return redirect("/home/")# or your url name

		else:
			messages.error(request, 'Error wrong username/password')
	context = {}
	context['form']=form

	return render(request, 'login.html', context)

	
@user_passes_test(lambda u: u.is_staff)
def StaffHome(request):
	context = {}
	return render(request, 'home.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AdminHome(request):
	context = {}
	return render(request, 'userlist.html', context)


class BikeView(CreateView):
	template_name='bike.html'
	form_class= BikeForm
	success_url = 'bike'

class BikeListView(ListView):
	template_name = 'bikelist.html'
	model = Bike

class DetailView(View):
	template_name = 'detail.html'

	def get(self,request,uid):
		bik = Bike.objects.get(id=uid)
		context ={
		'data': bik
		}
		return render(request,self.template_name,context)

class DetailView2(DetailView):
	template_name = 'detail.html'
	model  = Bike
	context_object_name = 'data'
