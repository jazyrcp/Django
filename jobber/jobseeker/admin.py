# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from jobseeker.models import Seeker,Application,Review

# Register your models here.
admin.site.register(Seeker)
admin.site.register(Application)
admin.site.register(Review)
