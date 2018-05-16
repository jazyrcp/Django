# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app1.models import First,Second,Third

# Register your models here.
admin.site.register(First)
admin.site.register(Second)
admin.site.register(Third)