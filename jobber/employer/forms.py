from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from employer.models import Employer,Job

class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']


class EmployerCreateForm(forms.ModelForm):

	class Meta:
		model = Employer
		fields = ['e_firm','e_detail','e_place']
		labels = {
		'e_firm': 'Company Name',
		'e_detail':'Company Details',
		'e_place':'Location'
		}


class EmployerForm(forms.Form):

	first_name = forms.CharField(label="First Name",widget=forms.TextInput() ,required=True)
	last_name = forms.CharField(label="Last Name",widget=forms.TextInput() ,required=True)
	email = forms.EmailField(label="Email ID",widget=forms.TextInput(),required=True)
	e_firm = forms.CharField(label="Company Name",widget=forms.TextInput() ,required=True)
	e_detail = forms.CharField(label="Company Details",widget=forms.Textarea() ,required=True)
	e_place = forms.CharField(label="Location",widget=forms.TextInput() ,required=True)
	username = forms.CharField(label="Username",widget=forms.TextInput() ,required=True)
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput() ,required=True)
	password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput() ,required=True)


class NewJobForm(forms.ModelForm):
	
	class Meta():
		model = Job
		fields = ['j_name','j_subcat','j_detail','j_requirement','j_salary']
		labels = {
		'j_name':'Job Name',
		'j_subcat':'Job Category',
		'j_detail':'Job Description',
		'j_requirement':'Requirements',
		'j_salary':'Salary per Month'
		}