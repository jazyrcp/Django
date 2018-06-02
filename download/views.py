from django.views.generic import View, TemplateView
from django.shortcuts import render,redirect,get_object_or_404, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# from registration.models import *
from django import http
from models import Employee,Department,LeaveRequest,LeaveType,EmpHead
from forms import EmployeeForm,DeptForm,LeaveRequestForm,LoginForm,LeaveTypeForm,AssignEmpHeadForm
import json
from django.contrib.auth import authenticate 
from mongoengine import connect
from django.db.models import Q
from bson.objectid import ObjectId
from django.contrib import messages

connect('employe')

# class HomeView(View):
# 	template_name = 'index1.html'
# 	def get(self,request):
# 		return render(request,self.template_name)


class NewDept(View):
	template_name = 'deptcreate.html'
	form_class =DeptForm
	def get(self, request):
		if request.user.is_superuser:
			form = self.form_class()

			context = {
				'form': form
			}
			return render(request,self.template_name,context)
		else:
			return redirect("login")

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			context = {
				'form':form,
				'success':"saved successfully"
			}
			return render(request,self.template_name,context)

		else:
			context = {
				'form':form
			}
			return render(request,self.template_name,context)

class ShowEmployees(View):
	template_name =  'employeelist.html'
	def get(self,request):
		if request.user.is_superuser:
			empobjt=Employee.objects.get(usr_id=ObjectId(request.user.id))
			emp=Employee.objects.exclude(id=ObjectId(empobjt.id))
			context = {
				'emp':emp
			}
			return render(request, self.template_name, context)
		else:
			return redirect("login")
		



class NewRegistration(View):
	template_name = 'employeeregister.html'
	form_class = EmployeeForm

	def get(self,request):
		if request.user.is_superuser:
			form=self.form_class()
			context={
			 'form':form
			}
			return render(request,self.template_name,context)
		else:
			return redirect("login")

	def post(self,request):
		form = self.form_class(request.POST,request.FILES)
		# print "request++++++++++++++++",request
		if form.is_valid():
			# print"VALID"
			user = User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('pwd1'),
				first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),email=request.POST.get('email'))

			qual=form.cleaned_data['qualification']
			# deptment= form.cleaned_data['dept']
			
			deptobj= Department.objects.get(id=form.cleaned_data['dept'])
			# print "FFFFFFFFFFFFFFFFF",deptobj
			emp = Employee.objects.create(
				usr = user,
				address = request.POST.get('address'),
				gender = request.POST.get('gender'),
				dob = request.POST.get('dob'),
				qualification = qual,
				mobile_no = request.POST.get('mobile_no'),
				dept =deptobj,
				)
			emp.save()
			context = {
				'form':form,
				'success':"saved successfully"
			}
			return render(request,self.template_name,context)

		else:
			context = {
				'form':form
			}
			return render(request,self.template_name,context)
			# print form.errors
			# return HttpResponse("not valid")
		# return HttpResponse("Ok")


class ApplyLeave(View):
	template_name = 'leave_request.html'
	form_class = LeaveRequestForm

	def get(self,request):
		
		if request.user.is_authenticated():
			
			form=self.form_class()
			context={
			 'form':form
			}
			return render(request,self.template_name,context)
		else:
			return redirect("login")

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid:
			# print "RRRRRRRRRRRR",request.user.username

			empobjt=Employee.objects.get(usr_id=ObjectId(request.user.id))
			# print "KJJJJJJJJJJJJJJJJJJJJJJ",empobjt.id
			eid=empobjt.id
			lv_rq_objt=LeaveRequest.objects.filter(emp_id=eid)
			print "AVAILLEAV",lv_rq_objt
			
			if lv_rq_objt:

				available = lv_rq_objt[0].avail_leave
				print "available",available
				emp_obj=Employee.objects.get(id=eid)
				depart=emp_obj.dept.name
				# print "DEPARTMENT",depart
				dept_obj=Department.objects.get(name=depart)
				ltyp=request.POST.get('ltype')
				# print "NNNNNNNNNNN",request.POST.get('ltype')
				lev_req_obj=LeaveRequest.objects.create(

					emp = emp_obj,
					dept=dept_obj,
					leave_from = request.POST.get('leave_from'),
					leave_to = request.POST.get('leave_to'),
					no_of_days = request.POST.get('no_of_days'),
					ltype=LeaveType.objects.get(id=ltyp),
					avail_leave=available,
					reason = request.POST.get('reason')
					)
				lev_req_obj.save()
			else:
				emp_obj=Employee.objects.get(id=eid)
				depart=emp_obj.dept.name
				# print "DEPARTMENT",depart
				dept_obj=Department.objects.get(name=depart)
				ltyp=request.POST.get('ltype')
				# print "NNNNNNNNNNN",request.POST.get('ltype')
				lev_req_obj=LeaveRequest.objects.create(

					emp = emp_obj,
					dept=dept_obj,
					leave_from = request.POST.get('leave_from'),
					leave_to = request.POST.get('leave_to'),
					no_of_days = request.POST.get('no_of_days'),
					ltype=LeaveType.objects.get(id=ltyp),
					reason = request.POST.get('reason')
					)
				lev_req_obj.save()

			context = {
			'form':form,
			'success':"Leave request submitted successfully",
			}
			return render(request,self.template_name,context)

		else:
			context = {
			'form':form
			}
			return render(request,self.template_name,context)
			# print form.errors
			# return HttpResponse("not valid")
		# return HttpResponse("Ok")

class LoginView(View):
	
	form_class=LoginForm

	def get(self,request):
		if request.user.is_authenticated():
			if request.user.is_superuser:
				return redirect("admin_home")
			else:
				empobj=Employee.objects.get(usr_id=ObjectId(request.user.id))
				try:
					headobj=EmpHead.objects.get(employee_id=ObjectId(empobj.id))
					if headobj:
						return redirect("head_home")
				except ObjectDoesNotExist:
					return redirect ("emp_home")
				# logeduser = request.user.first_name
				# lastname=request.user.last_name
				# email = request.user.email

				# userobj=User.objects.filter(username=request.user.username)
				# uservalues=userobj.values('id')
			

				# context={

				# 	'logeduser':logeduser,
				# 	'lastname':lastname,
				# 	'email': email,

				# }
				# return render(request,self.template_name,context)
			
		# return HttpResponse("Ok")

class ShowAllLeaveRequests(View):
	template_name =  'showleaves.html'
	def get(self,request):
		# print "kjhsdkjhf",request.user.is_superuser
		# print "UUUUUUUUU",request.user.id
		empobj=Employee.objects.get(usr_id=ObjectId(request.user.id))
		# print "NAMEEEEEEEEE",empobj.usr.first_name
		# print "deptname",empobj.dept.name
		if request.user.is_superuser:
			leavereq=LeaveRequest.objects.filter(Q(status="Accepted")|Q(status="Rejected"))
			context = {
				'leavereq':leavereq
			}
			return render(request, self.template_name, context)
		else:
			return redirect("login")


# class ShowNewLeaveRequests(View):
# 	template_name =  'shownewleaves.html'
# 	def get(self,request):
# 		if request.user.is_superuser:


			
# 			leavereq=LeaveRequest.objects.filter(status="Requested")
# 			context = {
# 				'leavereq':leavereq
# 			}
# 			return render(request, self.template_name, context)
# 		else:
# 			return redirect("login")


class LeaveApprove(View):
	def get(self,request,id):
		
		leave_req_id=id
		rqstobj=LeaveRequest.objects.get(id=leave_req_id)

		total=rqstobj.total_leave
		noofdays=rqstobj.no_of_days
		remaindays=total-noofdays

		rqstobj.avail_leave=remaindays
		rqstobj.status="Accepted"

		rqstobj.save()

		messages.success(request, 'Leave Approved')
		return http.HttpResponseRedirect(reverse('dept_leave_request_show'))


class LeaveReject(View):
	def get(self,request,id):
		leave_id=id
		rqst_obj=LeaveRequest.objects.get(id=leave_id)

		rqst_obj.status="Rejected"
		rqst_obj.save()
		messages.success(request, 'Leave Rejected')
		return http.HttpResponseRedirect(reverse('dept_leave_request_show'))

# class LeaveDelete(View):
# 	def get(self,request,id):
# 		if request.user.is_superuser:
# 			leave_id=id
# 			rqst_obj=LeaveRequest.objects.get(id=leave_id).delete()
# 			return redirect('leave_request_show')
			

class MyLeaveStatus(View):
	template_name = 'myleavestatus.html'
	def get(self,request):
		if request.user.is_authenticated():
			# print "HHHHHHHHHHHHHHHHHHHHHH",request.user.id
			empobj=Employee.objects.get(usr_id=ObjectId(request.user.id))
			# print "DSSSSSSSSSDSDSDSDSDSD",empobj.id

			rqst_obj= LeaveRequest.objects.filter(emp_id=ObjectId(empobj.id))
			# print "DSSSSPPPPPPPPPPPPPPSDSDSDSDSD",rqst_obj
			context={
			'rqst_obj':rqst_obj
			}
			return render(request,self.template_name,context)
		else:
			return redirect("login")

class AdminHomeView(View):
	template_name='adminhome.html'
	def get(self,request):
		return render(request,self.template_name)
	

class EmpHomeView(View):
	template_name='employeehome.html'
	def get(self,request):
		return render(request,self.template_name)

class DeptHeadHomeView(View):
	template_name='dept_head_home.html'
	def get(self,request):
		return render(request,self.template_name)

class MyProfileView(View):
	template_name='myprofile.html'
	def get(self,request):
		if request.user.is_authenticated():
			print "username",request.user.username
			print "uid====",request.user.id
			empobjt=Employee.objects.get(usr_id=ObjectId(request.user.id))
			context={
			'empobjt':empobjt
			}
			return render(request,self.template_name,context)
		else:
			return redirect("login")

class ShowDept(View):
	template_name =  'showdepartment.html'
	def get(self,request):
		if request.user.is_superuser:
			dept_obj=Department.objects.all()
			context = {
				'dept_obj':dept_obj
			}
			return render(request, self.template_name, context)
		else:
			return redirect("login")

class DeleteDept(View):
	def get(self,request,id):
		dept_id=id
		dept_obj=Department.objects.get(id=dept_id).delete()
		return redirect('show_dept')

class EmployeeDelete(View):
	def get(self,request,id):
		emp_id=id
		dept_obj=Employee.objects.get(id=emp_id).delete()
		return redirect('employee_show')

# class EditDept(View):
# 	template_name = 'editdepartment.html'
# 	form_class = DeptForm
# 	def get(self,request,id):
# 		if request.user.is_superuser:
# 			form = self.form_class()

# 			context = {
# 				'form': form
# 			}
# 			return render(request,self.template_name,context)
# 		else:
# 			return redirect("emp_home")


class NewLeaveType(View):
	template_name = 'NewLeaveType.html'
	form_class = LeaveTypeForm
	def get(self,request):
		if request.user.is_superuser:
			form = self.form_class()

			context = {
				'form': form
			}
			return render(request,self.template_name,context)
		else:
			return redirect("login")

	def post(self,request):
		form = self.form_class(request.POST)
		# print "JHHHHHHH",request.POST
		if form.is_valid():
			form.save()
			context = {
				'form':form,
				'success':"Leave type added successfully"
			}
			return render(request,self.template_name,context)

		else:
			# print "//////////////////////",form.errors
			context = {
				'form':form
			}
			return render(request,self.template_name,context)



class CancelLeave(View):
	def get(self,request,id):
		if request.user.is_authenticated():
			leave_id=id
			rqst_obj=LeaveRequest.objects.get(id=leave_id).delete()
			return redirect('emp_leave_status')

class AssignEmpHead(View):
	template_name = "assign_emp_head.html"
	form_class =AssignEmpHeadForm
	def get(self,request):
		if request.user.is_superuser:
			form=self.form_class()
			context={
			 'form':form,
			}
			return render(request,self.template_name,context)
		else:
			return redirect('login')
	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			deptobj=Department.objects.get(id=request.POST.get('department'))
			empobj=Employee.objects.get(id=request.POST.get('employee'))
			try:
				empheadobj=EmpHead.objects.get(department_id=request.POST.get('department'))
				if empheadobj:
					empheadobj.employee =empobj
					empheadobj.save()
			except ObjectDoesNotExist:
				assin_emp_obj=EmpHead.objects.create(
					department =deptobj,
					employee =empobj
				)
				assin_emp_obj.save()
			context = {
				'form':form,
				'success':"Employee is assigned as Department Head"
			}
			return render(request,self.template_name,context)
		else:
			context = {
				'form':form
			}
			return render(request,self.template_name,context)


		



class SelectEmp(View):
	def get(self,request):
		dep_id=request.GET.get('dept_id')
		emp_objt = Employee.objects.raw_query({'dept.id': ObjectId(dep_id)})
		empObjects = []
		for emp in emp_objt:
			emp_dict = {}
			emp_dict['id'] = emp.id
			emp_dict['name'] = emp.usr.first_name
		   
			empObjects.append(emp_dict)
		return HttpResponse(json.dumps(empObjects))
		


class EmployeeEdit(View):
	template_name='EditEmployee.html'
	form_class=EmployeeForm
	def get(self,request,id):
		if request.user.is_superuser:
			empid=id

			emp_obj=Employee.objects.get(pk=id)

			choices = [(dept.id, str(dept.name)) for dept in Department.objects.filter(name=emp_obj.dept.name)]
			print choices
			form = EmployeeForm(
				initial={
				'first_name':emp_obj.usr.first_name,
				'last_name':emp_obj.usr.last_name,
				'address':emp_obj.address,
				'dob':emp_obj.dob,
				'mobile_no':emp_obj.mobile_no,
				'dept':emp_obj.dept.id,
				# 'username':emp_obj.usr.username,
				# 'password':emp_obj.usr.password,
				# 'gender':emp_obj.gender,
				# 'email':emp_obj.usr.email,
				# 'edit':True,
				}
			)
			context = {
				'form': form
			}
			return render(request,self.template_name,context)
		else:
			return redirect('login')

	def post(self,request,id):
		if request.user.is_superuser:
			empid=id
			form = EmployeeForm(request.POST)
			print "FORNM",request.POST
			emp=Employee.objects.get(id=empid)
			print emp
			edit_user = User.objects.filter(id=emp.usr_id)
			print "editttttttttttttt",edit_user.values('first_name')
			# form.emailedit=emp.usr_email
			if form.is_valid():

				print "valid"
				edit_user.first_name=request.POST.get('first_name'),
				edit_user.last_name=request.POST.get('last_name'),
				# edit_user.email=request.POST.get('email'),
				# edit_user.save()
				# emp.address=request.POST.get('address'),
				# emp.dob=request.POST.get('dob'),
				# emp.mobile_no=request.POST.get('mobile_no'),
				# emp.dept=request.POST.get('dept')
				# emp.save()
				form.save()

				context = {
				'form': form
				}
				return render(request,self.template_name,context)
			else:
				print "not cvalid",form.errors
				context = {
				'form':form
				}
				return render(request,self.template_name,context)
		else:
			return redirect('emp_home')

class ShowDeptLeaveRequests(View):
	template_name = 'HeadViewNewRequest.html'
	def get(self,request):
		# print "UUUUUUUUid",request.user.id
		if request.user.is_authenticated():
			empobj=Employee.objects.get(usr_id=ObjectId(request.user.id))
			try:
				headobj=EmpHead.objects.get(employee_id=ObjectId(empobj.id))
				if headobj:
					dept_hod=headobj.department.name
					# print "DDDDDDDD",dept_hod
					# print "eeee",empobj.dept.name
					leavereq=LeaveRequest.objects.filter(dept_id=headobj.department.id,status="Requested")
					# lv_obj=LeaveRequest.objects.get(emp_id.gender='female')
					# print "nnnnnnnnn",lv_obj
					context = {
					'leavereq':leavereq
					}
					return render(request, self.template_name, context)
			except ObjectDoesNotExist:
				return redirect("login")
		else:
			return redirect("login")

class ShowDeptAllLeaves(View):
	template_name = 'HeadViewAllLeaves.html'
	def get(self,request):
		if request.user.is_authenticated():
			empobj=Employee.objects.get(usr_id=ObjectId(request.user.id))
			try:
				headobj=EmpHead.objects.get(employee_id=ObjectId(empobj.id))
				if headobj:
					dept_hod=headobj.department.name
					leavereq=LeaveRequest.objects.filter(Q(status="Accepted")|Q(status="Rejected"))
					context = {
					'leavereq':leavereq
					}
					return render(request, self.template_name, context)
			except ObjectDoesNotExist:
				return redirect("login")
		else:
			return redirect("login")

class ShowEmployeesByDept(View):
	template_name ='EmployeesByDept.html'
	def get(self,request):
		if request.user.is_authenticated():
			empobj=Employee.objects.get(usr_id=ObjectId(request.user.id))
			try:
				headobj=EmpHead.objects.get(employee_id=ObjectId(empobj.id))
				if headobj:
					dept_hod=headobj.department.name
					empobj=Employee.objects.raw_query({'dept.name':dept_hod})
					print "kjkjhkjhkj",empobj
					context = {
						'empobj':empobj
					}
					return render(request, self.template_name, context)
			except ObjectDoesNotExist:
				return redirect("login")
		else:
			return redirect("login")









