from django import forms

from appfour.models import Brand,Car,Bike
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BrandForm(forms.ModelForm):
	class Meta:
		model = Brand
		fields= ['name']


class CarForm(forms.ModelForm):
	class Meta:
		model = Car
		fields= ['brand','name','engine_cc','wheel_size','color']


class BigForm(forms.Form):

	brand_name = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Brand Name','class':'form-control'}),required = True)
	car_name = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Car Name','class':'form-control'}),required = True)
	engine = forms.IntegerField(widget = forms.TextInput(attrs = {'placeholder':'Engine Capacity','class':'form-control'}),required = True)
	wheel_size = forms.IntegerField(widget = forms.TextInput(attrs = {'placeholder':'Wheel Size','class':'form-control'}),required = True)
	color = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Color','class':'form-control'}),required = True)


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']

class BikeForm(forms.ModelForm):
	class Meta:
		model = Bike
		fields = ['brand','bname','engine_cc','color']