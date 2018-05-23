from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from shopname.models import Product

CAT = (('men','Men'),('women','Women'),('kids','Kids'))
SUB = (('casual','Casual'),('formal','Formal'),('sports','Sports'))

class UserForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password1','password2'] 


class NewProductForm(forms.Form):

	pro_name = forms.CharField(label  = 'Product name',widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
	pro_brand = forms.CharField(label = 'Brand name',widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
	pro_cat = forms.ChoiceField(label = 'Category',widget=forms.RadioSelect,choices = CAT,required=True)
	pro_sub = forms.ChoiceField(label = 'SubCategory',widget=forms.RadioSelect,choices = SUB,required=True)
	pro_detail = forms.CharField(label = 'Detail',widget=forms.Textarea(attrs={'class':'form-control'}),required=True)
	pro_color = forms.CharField(label = 'Color',widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
	pro_price = forms.IntegerField(label = 'Price',widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
	pro_image = forms.ImageField(label = 'Image',required=True)
