# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView,View,CreateView
from forms import SampleForm

# Create your views here.


class HomeView(View):
	template_name='home.html'

	def get(self,request):
		return render(request,self.template_name)


class SampleView(CreateView):
	template_name='sample_new.html'
	form_class=SampleForm
	success_url='success'