from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField,EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager
# from models import Department

# from leave.models import Department
# from employee_app.common.models import BASIC_TYPES

class Department(models.Model):
	name=models.CharField(max_length=100)

	objects = MongoDBManager()

# class Qualification(models.Model):
# 	qual_text=models.CharField(max_length=100)
# 	objects = MongoDBManager()

class Employee(models.Model):
	
	usr =  models.OneToOneField(User)
	address = models.CharField(max_length=100)
	gender =models.CharField(max_length=100)
	dob = models.DateField(null=True,blank=True)
	qualification = ListField()
	dept = EmbeddedModelField(Department)
	mobile_no = models.CharField(max_length=100)
	date_of_join = models.DateField(null=True,blank=True,auto_now_add=True)

	objects = MongoDBManager()
	
class LeaveType(models.Model):
	ltype=models.CharField(max_length=200)

	objects = MongoDBManager()

class LeaveRequest(models.Model):
	emp=models.OneToOneField(Employee)
	dept=models.OneToOneField(Department)
	leave_from = models.DateField(null=True,blank=True)
	leave_to = models.DateField(null=True,blank=True)
	no_of_days = models.IntegerField()
	ltype=models.OneToOneField(LeaveType)
	avail_leave = models.IntegerField(default=12)
	total_leave = models.IntegerField(default=12)
	reason = models.CharField(max_length=200)
	status = models.CharField(max_length=200,default='Requested')

	objects = MongoDBManager()

class EmpHead(models.Model):
	department=models.OneToOneField(Department)
	employee=models.OneToOneField(Employee)
	
	objects = MongoDBManager()










