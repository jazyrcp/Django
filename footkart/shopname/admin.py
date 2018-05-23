# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from shopname.models import Category,SubCategory,Product,Cart
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Cart)