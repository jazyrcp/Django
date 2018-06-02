# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,View,DetailView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from employer.models import Job,Employer,Category,SubCategory
from jobseeker.models import Seeker,Application,Review
from jobseeker.forms import SeekerForm,ApplyForm,ReviewForm


# Create your views here.

class HomeView(ListView):
	template_name = 'home.html'
	
	def get(self,request):
		job = Job.objects.order_by('-j_created')
		emp = Employer.objects.all()[:5]
		cat = Category.objects.all()
		return render(request,self.template_name,{'job':job,'emp':emp,'cat':cat})

	def post(self,request):
		query = request.POST.get('se1')
		print(query)
		job = Job.objects.filter(j_name__icontains = query).order_by('-j_created')
		emp = Employer.objects.all()[:5]
		cat = Category.objects.all()
		return render(request,self.template_name,{'job':job,'emp':emp,'cat':cat,'query':query})


class SeekerCreateView(View):
	template_name = 'usercreate.html'
	form_class = SeekerForm

	def get(self,request):
		form = self.form_class()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			usr = User.objects.create_user(username = request.POST.get('username'),first_name = request.POST.get('first_name'),
				last_name = request.POST.get('last_name'),email = request.POST.get('email'),password = request.POST.get('password1'))
			sek = Seeker.objects.create(
				s_user = usr,
				s_qualification = request.POST.get('s_qualification'),
				s_experience = request.POST.get('s_experience'),
				s_ph = request.POST.get('s_ph'),
				s_resume = request.FILES.get('s_resume'),
				s_image = request.FILES.get('s_image'),
				)

			
			sek.save()

			return redirect('home')

		else:
			form = self.form_class()
			return render(request,self.template_name,{'form':form})

class ApplyView(View):
	template_name = 'applyjob.html'
	form_class = ApplyForm
	

	def get(self,request,jid):
		form = self.form_class()
		j_obj = Job.objects.get(id =jid)
		return render(request,self.template_name,{'obj':j_obj,'form':form})

	def post(self,request,jid):


		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			

			
			job = Job.objects.get(id =jid)
			
			form.a_job = job

			s = request.user
			usr =User.objects.get(username = s)
			
			sek = Seeker.objects.get(s_user = usr)
			form.a_seeker = sek
			app = Application.objects.create(
				a_job = job,
				a_seeker = sek,
				a_resume = request.FILES.get('a_resume'),
				a_cover = request.POST.get('a_cover'),
				)
			app.save()


			

			return redirect('home')

		else:
			form = self.form_class()
			return render(request,self.template_name,{'form':form})


class ReviewView(View):
	template_name = 'review.html'
	form_class = ReviewForm

	def get(self,request,fid):
		form = self.form_class()
		firm = Employer.objects.get(id = fid)
		return render(request,self.template_name,{'form':form,'firm':firm})

	def post(self,request,fid):
		form = self.form_class(request.POST)
		if form.is_valid():
			detail = request.POST.get('r_detail')
			firm = Employer.objects.get(id = fid)
			s = request.user
			usr = User.objects.get(username = s)
			sek = Seeker.objects.get(s_user = usr)

			rev = Review.objects.create(
				r_seeker = sek,
				r_firm = firm,
				r_detail = detail,
				)
			rev.save()
			return redirect('home')

		else:
			form  =form_class()
			return render(request,self.template_name,{'form':form,'firm':firm})


class JobView(View):
	template_name = 'jobs.html'

	def get(self,request,cid):

		cat = Category.objects.all()
		catj = Category.objects.get(c_name = cid)
		sub = SubCategory.objects.filter(s_cat =catj)
		
		emp = Employer.objects.all()[:5]
		return render(request,self.template_name,{'job':sub,'emp':emp,'cat':cat})

	def post(self,request,cid):
		query = request.POST.get('se1')
		print(query)
		job = Job.objects.filter(j_name__icontains = query).order_by('-j_created')
		emp = Employer.objects.all()[:5]
		cat = Category.objects.all()
		return render(request,'home.html',{'job':job,'emp':emp,'cat':cat,'query':query})



class EmployerView(DetailView):
	template_name = 'employer.html'
	model = Employer
	context_object_name = 'data'

from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from django.http import HttpResponse

class SearchView(View):
	template_name = 'home.html'

	def post(self,request):
		quote = request.POST.get('q')
		print(quote)
		jobs = Job.objects.filter(j_name__icontains = quote).order_by('-j_created').values()
		print(jobs)
		# job = Job.objects.all().order_by('-j_created')
		emp = Employer.objects.all()[:5]
		cat = Category.objects.all()
		# return render(request,self.template_name,{'job':job,'emp':emp,'cat':cat})
		return redirect('elogin')
	
class ChangePwd(View):
	
	template_name = 'changepwd.html'

	def get(self,request):
		return render(request,self.template_name)

	def post(self,request):

		pwd1 = request.POST.get('pwd1')
		pwd2 = request.POST.get('pwd2')
		pwd3 = request.POST.get('pwd3')
		

		u = request.user
		usr = User.objects.get(username = u)
		print(usr.password)
		if usr.check_password(pwd1):
			if pwd2==pwd3:
				print(usr.password)
				usr.set_password(pwd2)
				usr.save()
				return redirect('/login/')

			else:
				return render(request,self.template_name,{'p3':'Passwords does not match'})

		else:
			return render(request,self.template_name,{'p3':'Incorrect Password'})
		data = {'job':list(jobs)}
		
		return JsonResponse(data)
	# 	# return render(request,self.template_name,{'job':job,'emp':emp,'cat':cat})
	# 	return redirect('elogin')
	# 

