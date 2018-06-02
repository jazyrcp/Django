# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,View
from appone.forms import StudentForm
from appone.models import Student
# Create your views here.
class HomeView(TemplateView):
	template_name='home.html'

# class StudentView(CreateView):
# 	template_name='student.html'
# 	form_class=StudentForm
# 	success_url='/student'

class StudentListView(ListView):
	template_name='stud_list.html'
	model=Student

class StudentView(View):
	template_name='student.html'

	def get(self,request):
		form=StudentForm()
		context={'form':form}
		return render(request,self.template_name,context)