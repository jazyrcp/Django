from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from appone.models import Student,Teacher,Prince


class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=['name','place']


class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ['name','dept','image']


class HodForm(forms.Form):

	first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),required=True)
	last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}),required=True)
	email=forms.EmailField(label='E-mail Id',widget=forms.TextInput(attrs={'placeholder':'mail Id','class':'form-control'}),required=True)
	dept=forms.CharField(label='Department',widget=forms.TextInput(attrs={'placeholder':'Department name','class':'form-control'}),required=True)
	username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Department name','class':'form-control'}),required=True)
	pwd1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class':'form-control'}),required=True)
	pwd2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder':'Re-enter your Password','class':'form-control'}),required=True)


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']


class PrinceForm(forms.ModelForm):
	class Meta:
		model = Prince
		fields = ['country']