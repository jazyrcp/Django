from django import forms

from footshop.models import Product,Category,SubCategory

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['pro_name','pro_brand','pro_cat','pro_image','pro_detail']

class CategoryForm(forms.ModelForm):
	class Meta:
		model =Category
		fields = ['cat_name']


class SubCategoryForm(forms.ModelForm):
	class Meta:
		model = SubCategory
		fields =['sub_cat','sub_name','sub_desc']
# class ProductForm(forms.Form):


# 	pro_name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'placeholder':'Product Name','class':'form-control'}),required=True)
# 	pro_brand=forms.CharField(label='Brand',widget=forms.TextInput(attrs={'placeholder':'Brand Name','class':'form-control'}),required=True)
# 	pro_cat=forms.ChoiceField(label='Category',widget=forms.RadioSelect,choices=CATEGORY),required=True)
# 	pro_typ=forms.ChoiceField(label='For',widget=forms.RadioSelect,choices=TYPE),required=True)
# 	pro_size=forms.ChoiceField(label='Size',widget=forms.RadioSelect,choices=SIZE),required=True)
# 	pro_image=forms.ImageField(label='Image')