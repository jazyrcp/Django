# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from appfour.models import Brand,Car,Bike
# Register your models here.
admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Bike)
