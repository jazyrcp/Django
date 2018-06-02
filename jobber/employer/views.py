# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,FormView,CreateView,ListView
from employer.forms import UserForm,EmployerCreateForm,EmployerForm,NewJobForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth,messages
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse

from employer.models import Employer,Job,SubCategory,Category
from jobseeker.models import Seeker




class EmpZoneView(ListView):
	template_name = 'ezone.html'

	def get(self,request):
		if request.user.is_authenticated():
			s = request.user
			usr = User.objects.get(username = s)
			emp = Employer.objects.get(e_user  = usr)
			jobs = Job.objects.filter(j_employer = emp).order_by('-j_created')
			return render(request,self.template_name,{'jobs':jobs})
				
		else:
			return render(request,self.template_name)

# class EmpCreateView(FormView):
# 	template_name ='empcreate.html'
# 	form_class = UserForm

# 	def get(self,request,*args, **kwargs):
# 		self.object = None
# 		form_class = self.get_form_class()
# 		u_form = self.get_form(form_class)
# 		e_form = EmployerCreateForm()
# 		return self.render_to_response(
# 			self.get_context_data(form1=u_form, form2=e_form))


# 	def post(self,request,*args,**kwargs):
# 		self.object = None
# 		form_class = self.get_form_class()
# 		u_form = self.get_form(form_class)
# 		e_form = EmployerCreateForm(self.request.POST)
# 		if (u_form.is_valid() and e_form.is_valid()):
# 			return self.form_valid(u_form, e_form)
# 		else:
# 			return self.form_invalid(u_form, e_form)

# 	def get_success_url(self,**kwargs):
# 		return  'success' 


# 	def form_valid(self, u_form, e_form):
# 		self.object = u_form.save()
# 		self.object.is_staff=True
# 		self.object.save()
# 		p = e_form.save(commit=False)
# 		p.user = self.object
# 		p.save()
# 		return super(EmpCreateView, self).form_valid(u_form)

# 	def form_invalid(self, u_form, e_form):
# 		return self.render_to_response(self.get_context_data(form1=u_form,  form2=e_form))


class EmpCreateView(View):
	template_name = 'empcreate.html'
	form_class = EmployerForm

	def get(self,request):
		form = self.form_class()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			usr = User.objects.create_user(username = request.POST.get('username'),first_name = request.POST.get('first_name'),
				last_name = request.POST.get('last_name'),email = request.POST.get('email'),password = request.POST.get('password1'))
			usr.is_staff=True
			usr.save()
			emp = Employer.objects.create(
				e_user = usr,
				e_firm = request.POST.get('e_firm'),
				e_place = request.POST.get('e_place'),
				e_detail = request.POST.get('e_detail'))

			
			emp.save()

			return redirect('ezone')

		else:
			form = self.form_class()
			return render(request,self.template_name,{'form':form})


class NewJobView(View):
	template_name = 'newjob.html'
	form_class = NewJobForm
	
	def get(self,request):
		form=self.form_class()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			usr = request.user
			emp = Employer.objects.get(e_user = usr)
			cat = SubCategory.objects.get(id = request.POST.get('j_subcat'))
			job = Job.objects.create(
				j_employer = emp,
				j_name=request.POST.get('j_name'),
				j_subcat=cat,
				j_requirement=request.POST.get('j_requirement'),
				j_detail=request.POST.get('j_detail'),
				j_salary = request.POST.get('j_salary')
				)
			job.save()
			return redirect('/ezone/')
		else:
			form=form_class()
			return render(request,self.template_name,{'form':form})


def login(request):
    form =AuthenticationForm()
    if request.user.is_authenticated():
        if request.user.is_staff:
            return redirect("/ezone/")# or your url name
        else:
            return redirect("/home/")# or your url name


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            if request.user.is_staff:
                return redirect("/ezone/")# or your url name
            else:
                return redirect("/home/")# or your url name

        else:
            messages.error(request, 'Error wrong username/password')
    context = {}
    context['form']=form

    return render(request, 'elogin.html', context)


class ApplicationView(View):
	template_name = 'applications.html'

	def get(self,request):
		s = request.user
		usr = User.objects.get(username = s)
		emp = Employer.objects.get(e_user = usr)
		jb = emp.jobs.all().order_by('-j_created')
		return render(request,self.template_name,{'job':jb})


class ReviewView(View):
	template_name = 'viewreview.html'

	def get(self,request):
		s = request.user
		usr = User.objects.get(username = s)
		emp = Employer.objects.get(e_user = usr)
		rev = emp.reviews.all().order_by('-r_created')
		return render(request,self.template_name,{"rev":rev})


class DeleteJob(View):

	def get(self,request,jid):

		job = Job.objects.get(id = jid).delete()
		return redirect('/ezone/')

class ProfileView(View):
	template_name = 'profile.html'

	def get(self,request,sid):
		sek  = Seeker.objects.get(id =sid)
		print(sek)
		return render(request,self.template_name,{'sek':sek})


class EditJob(View):
	template_name = 'newjob.html'
	form_class = NewJobForm

	def get(self,request,jid):
		job = Job.objects.get(id =jid)
		form = self.form_class(
			initial = {
			'j_name':job.j_name,
			'j_subcat':job.j_subcat,
			'j_detail':job.j_detail,
			'j_requirement':job.j_requirement,
			'j_salary':job.j_salary
			})
		return render(request,self.template_name,{'form':form})

	def post(self,request,jid):
		job = Job.objects.get(id =jid)
		form = self.form_class(request.POST)
		if form.is_valid():
			job.j_name = request.POST.get('j_name')
			cat = SubCategory.objects.get(id = request.POST.get('j_subcat'))
			job.j_subcat = cat
			
			job.j_detail = request.POST.get('j_detail')
			job.j_salary = request.POST.get('j_salary')
			job.j_requirement = request.POST.get('j_requirement')
			job.save()

			return redirect('/ezone/')

		else:
			return super.get(self,request,jid)


class SendMailView(View):

	def post(self,request):
		mail = request.POST.get('mail')
		j_id = request.POST.get('jid')
		job = Job.objects.get(id =j_id)
		print(mail)
		
		email = EmailMessage(job.j_name, job.j_detail, to=[mail])
		email.send()

		response = 'Success'
		return HttpResponse(json.dumps(response),content_type='json')


class ForgotPwdView(View):
	template_name = 'forgotpassword.html'

	def get(self,request):
		return render(request,self.template_name)

	def post(self,request):

		mail = request.POST.get('mail_id')
		print(mail)

		
		obj = User.objects.filter(email = mail)
		if obj.count()>0:
			for x in obj:
				print(x.email)
				email = EmailMessage('Forgot Password', x.password, to=[mail])
				email.send()
			return redirect('/login/')

		else:
			return render(request,self.template_name,{'obj':obj,'mail':mail})


class ChangePwd(View):
	
	template_name = 'changepwd.html'

	def get(self,request):
		return render(request,self.template_name)

	def post(self,request):

		pwd1 = request.POST.get('pwd1')
		pwd2 = request.POST.get('pwd2')
		pwd3 = request.POST.get('pwd3')
		

		u = request.user
		usr = User.objects.get(username = u)
		obj = usr.objects.get(password= pwd2)
		if obj.count()>0:
			usr.password = pwd1
			usr.save()
			return redirect('/login/')

		else:
			return render(request,self.template_name,{'obj':obj})