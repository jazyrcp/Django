from django import forms
from app1.models import First,Second,Third


class FirstForm(forms.ModelForm):
	class Meta:
		model=First
		fields=['name','place','image']

class SecondForm(forms.ModelForm):
	class Meta:
		model=Second
		fields=['name','place','image']

class ThirdForm(forms.ModelForm):
	class Meta:
		model= Third
		fields=['name','place']