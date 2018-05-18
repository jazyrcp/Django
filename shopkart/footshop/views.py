# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView

from footshop.forms import ProductForm,CategoryForm,SubCategoryForm

# Create your views here.


class ProductView(CreateView):
	template_name='newproduct.html'
	form_class= ProductForm

class CategoryView(CreateView):
	template_name='newcat.html'
	form_class=CategoryForm

class SubCatView(CreateView):
	template_name='newsub.html'
	form_class=SubCategoryForm