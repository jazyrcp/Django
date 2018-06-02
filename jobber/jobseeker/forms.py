from django import forms

from jobseeker.models import Application,Review


class SeekerForm(forms.Form):

	first_name = forms.CharField(label="First Name",widget=forms.TextInput() ,required=True)
	last_name = forms.CharField(label="Last Name",widget=forms.TextInput() ,required=True)
	email = forms.EmailField(label="Email ID",widget=forms.TextInput(),required=True)
	s_qualification = forms.CharField(label="Qualification",widget=forms.TextInput() ,required=True)
	s_experience = forms.CharField(label="Experience",widget=forms.Textarea() ,required=True)
	s_ph = forms.IntegerField(label="Contact No",widget=forms.TextInput() ,required=True)
	s_resume = forms.FileField(label="Resume",required=True)
	s_image = forms.ImageField(label="Photo")
	username = forms.CharField(label="Username",widget=forms.TextInput() ,required=True)
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput() ,required=True)
	password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput() ,required=True)


class ApplyForm(forms.ModelForm):

	class Meta:
		model = Application
		fields = ['a_cover','a_resume']
		labels = {
		'a_cover': 'Cover Letter',
		'a_resume':'Upload your resume'
		}

class ReviewForm(forms.ModelForm):

	class Meta:

		model = Review
		fields = ['r_detail']
		labels = {
		'r_detail' : 'Write your review below'
		}