# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from employer.models import Employer,Job,Category,SubCategory

# Register your models here.

admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(SubCategory)

