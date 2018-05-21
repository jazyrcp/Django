from django import forms
from django.contrib.auth.models import User
from footshop.models import Product,Category,SubCategory



GENDER=(('M','Male'),('F','Female'),('O','Other'),)

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['pro_name','pro_brand','pro_cat','pro_image','pro_detail','pro_color','pro_size','pro_price']
		labels = {
		'pro_name':'Product Name',
		'pro_brand':'Brand Name',
		'pro_cat':'For',
		'pro_image':'Product Image',
		'pro_detail':'Description',
		'pro_color':'Colour',
		'pro_size':'Size',
		'pro_price':'Price',
		}

class CategoryForm(forms.ModelForm):
	class Meta:
		model =Category
		fields = ['cat_name']


class SubCategoryForm(forms.ModelForm):
	class Meta:
		model = SubCategory
		fields =['sub_name']


# class ProductForm(forms.Form):


# 	pro_name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'placeholder':'Product Name','class':'form-control'}),required=True)
# 	pro_brand=forms.CharField(label='Brand',widget=forms.TextInput(attrs={'placeholder':'Brand Name','class':'form-control'}),required=True)
# 	pro_cat=forms.ChoiceField(label='Category',widget=forms.TextInput(attrs={'class':'form-control'}))
# 	pro_size=forms.ChoiceField(label='Size',widget=forms.RadioSelect,choices=SIZE)
# 	pro_image=forms.ImageField(label='Image',required=False)
# 	pro_detail=forms.CharField(label='Description',widget=forms.Textarea(attrs={'class':'form-control'}),required=True)


class CustomerForm(forms.Form):

	first_name = forms.CharField(label='First name',widget=forms.TextInput(attrs={'placeholder':'firstname','class':'form-control'}),required=True)
	last_name = forms.CharField(label='Last name',widget=forms.TextInput(attrs={'placeholder':'lastname','class':'form-control'}),required=True)
	email = forms.EmailField(label='Email ID',widget=forms.TextInput(attrs={'placeholder':'sample@gmail.com','class':'form-control'}),required=True)
	age = forms.CharField(label='Age',widget=forms.TextInput(attrs={'placeholder':'age','class':'form-control'}),required=True)
	gender = forms.ChoiceField(label='Gender',widget=forms.RadioSelect,choices=GENDER,required=True)
	place = forms.CharField(label='Address',widget=forms.Textarea(attrs={'placeholder':'address','class':'form-control'}),required=True)
	username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
	pwd1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
	pwd2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)

# class ProductListForm(forms.ModelForm):

# 	class Meta:
# 		model = Product
# 		fields =['pro_name','pro_brand','pro_cat','pro_sub','pro_image','pro_detail','pro_color','pro_size','pro_price']