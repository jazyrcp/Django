from django import forms

from appfour.models import Brand,Car

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