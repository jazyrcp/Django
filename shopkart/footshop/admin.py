# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from footshop.models import Customer,Category,Product,Cart
# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)

admin.site.register(Product)
admin.site.register(Cart)
