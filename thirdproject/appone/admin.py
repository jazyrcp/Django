# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from appone.models import Student,Teacher,Hod,Prince
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Hod)
admin.site.register(Prince)