# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView,ListView,View,TemplateView,FormView

from appone.forms import StudentForm,TeacherForm,HodForm,UserForm,PrinceForm
from appone.models import Student,Teacher,Hod
# Create your views here.


class HomeView(TemplateView):
	template_name='home.html'


# class StudentView(CreateView):
# 	template_name='studentin.html'
# 	form_class=StudentForm
# 	success_url='/student/create'


class StudentListView(ListView):
	template_name='table.html'
	def get(self,request):
		stud_obj = Student.objects.all()
		context = {'data': stud_obj}

		return render(request,self.template_name,context) 

# def studview(request):
# 	template_name = 'studentin.html'
# 	form = StudentForm()
# 	return render(request,template_name,{'form':form})

class StudentView(View):
	template_name = 'studentin.html'
	form_class = StudentForm()
	
	def get(self,request):
		form = self.form_class()
		context = {
		'form':form
		}
		return render(request,self.template_name,self.context)

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			context={
			'form':form,
			'success':"Saved Succesfully"
			}
		else:
			context={
			'form':form
			}
		return render(request,self.template_name,context)


class TeacherView(View):
	template_name = 'teacher.html'
	form_class = TeacherForm

	def get(self,request):
		form = self.form_class()
		context = {
		'form': form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			context = {
			'form':form,
			'success':"Succesfully Saved"
			}

		else:
			context={
			'form':form
			}
		return render(request,self.template_name,context)


class TeacherListView(View):
	template_name='teachlist.html'

	def get(self,request):
		teach = Teacher.objects.all()
		context = {
		'data':teach
		}
		return render(request,self.template_name,context)


class HodView(View):
	template_name='hod.html'
	form_class=HodForm

	def get(self,request):
		form = self.form_class()
		context = {
		'form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=request.POST.get('username'),first_name=request.POST.get('first_name'),
				last_name=request.POST.get('last_name'),email=request.POST.get('email'),password=request.POST.get('pwd1'))

			hodd=Hod.objects.create(
				usr=user,
				dept=request.POST.get('dept'),
				)
			hodd.save()
			context={
			'form':form,
			'success':'Saved Successfuly'
			}

			return render(request,self.template_name,context)

		else:
			context={
			'form':form
			}
			return render(request,self.template_name,context)


class HodListView(ListView):
	template_name='hodlist.html'
	model= Hod


class PrinceView(FormView):
	template_name ='prince.html'
	form_class = UserForm

	def get(self,request,*args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		user_form = self.get_form(form_class)
		p_form = PrinceForm()
		return self.render_to_response(
			self.get_context_data(form1=user_form, form2=p_form))


	def post(self,request,*args,**kwargs):
		self.object = None
		form_class = self.get_form_class()
		user_form = self.get_form(form_class)
		p_form = PrinceForm(self.request.POST)
		if (user_form.is_valid() and p_form.is_valid()):
			return self.form_valid(user_form, p_form)
		else:
			return self.form_invalid(user_form, p_form)

	def get_success_url(self, **kwargs):
		return reverse_lazy('login')

	def form_valid(self, user_form, p_form):
		self.object = user_form.save()
		self.object.is_staff=True
		self.object.save()
		p = p_form.save(commit=False)
		p.usr = self.object
		p.save()
		return super(PrinceView, self).form_valid(user_form)

	def form_invalid(self, user_form, p_form):
		return self.render_to_response(self.get_context_data(form1=user_form,  form2=p_form))
