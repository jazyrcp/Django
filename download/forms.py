from django import forms
from models import Employee,Department,LeaveType,LeaveRequest
from django.forms import TextInput,Select
import re
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
    instead of vertically.
    """

    def render(self):
        """Outputs radios"""
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class DeptForm(forms.ModelForm):
	class Meta:
		model=Department
		widgets={
		 'name': forms.TextInput(attrs={'class': 'form-control'})
		}

	def clean_name(self):
		if re.match(r"^([a-zA-Z\-0-9._ ]*)$", self.cleaned_data['name'].strip()):
			if Department.objects.filter(name__exact=self.cleaned_data['name']).count() > 0:
				raise forms.ValidationError('Department already exists')
			return self.cleaned_data['name'].strip()
		raise forms.ValidationError('Please enter a valid department_name')
		

class EmployeeForm(forms.Form):
	def __init__(self, *args, **kwargs):
		# dept_CHOICES=(('Human Resource','Human Resource',),('Software Development','Software Development',),('Documentation','Documentation'),('Testing','Testing',))
		qual_CHOICES=(('B.Sc','B.Sc',),('M.Sc','M.Sc',),('BTech','BTech',),('MTech','MTech',),('MCA','MCA',),('MBA','MBA',),('BBA','BBA',),('BCA','BCA',))
		super(EmployeeForm, self).__init__(*args, **kwargs)
		self.fields['qualification'].choices = qual_CHOICES
		# self.fields['dept'].choices = dept_CHOICES
		self.fields['dept'].choices = [(dept.id, str(dept.name)) for dept in Department.objects.all()]

	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your first name', 'class': 'form-control'}),required=True)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your last name', 'class': 'form-control'}),required=True)
	address =forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your address', 'class': 'form-control'}),required=True)
	gender_CHOICES = (('male', 'Male',), ('female', 'Female',),('other','Other'))
	gender = forms.ChoiceField( widget=forms.RadioSelect(renderer=HorizRadioRenderer, attrs={'data-fv-field':'gender'}), choices=gender_CHOICES,required=True)
	dob =  forms.CharField(label='Date of Birth',widget=forms.TextInput(attrs={'class': 'form-control datepicker','id':'dob','required':'required','placeholder':'YYYY-MM-DD','readonly':'true'}))
	qualification = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-selected-text-format':'count'}))
	mobile_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your mobileno', 'class': 'form-control'}),required=True)
	email=forms.EmailField(label='Email',required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Your e-mail ID', 'class': 'form-control  ','id':'ind_email','required':'required','maxlength' : '50'}))
	dept = forms.ChoiceField(required=True,widget=forms.Select(attrs={'class': 'selectpicker','data-selected-text-format':'count'}))
	username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your first name', 'class': 'form-control'}))
	pwd1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control ','id':'password'}))
	pwd2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password', 'class': 'form-control','id':'conf_password'}))
	
	edit=False
	def clean_first_name(self):
		if re.match(r"^[a-zA-Z. ]*$", self.cleaned_data['first_name'].strip()):
			return self.cleaned_data['first_name'].strip()
		raise forms.ValidationError('Enter Alphabets only')

	def clean_last_name(self):
		if re.match(r"^[a-zA-Z0-9. ]*$", self.cleaned_data['last_name'].strip()):
			return self.cleaned_data['last_name'].strip()
		raise forms.ValidationError('Enter Alphabets only')

	def clean_pwd1(self):
		if len(self.data['pwd1']) < 5:
			raise forms.ValidationError('Passwords must contain at least fivet characters')
		if (self.data['pwd1'] != self.data['pwd2']):
			raise forms.ValidationError('Passwords are not the same')
		return self.data['pwd1']

	def clean_username(self):
		if self.edit=="False" and User.objects.filter(username__exact=self.cleaned_data['username']).count() > 0:
			raise forms.ValidationError('Username already exists')

	def clean_mobile_no(self):
		if re.match(r"^([0-9+(). -]{6,12})$", self.cleaned_data['mobile_no'].strip()):
			if len(self.cleaned_data['mobile_no']) < 10:
				raise forms.ValidationError('Phone Number must contain at least eight digits')
			return self.cleaned_data['mobile_no'].strip()
		raise forms.ValidationError('Invalid Mobile No.')

	def clean_email(self):
		if self.edit=="False" and User.objects.filter(email__exact=self.cleaned_data['email']).count()>0:
			raise forms.ValidationError('e-mail ID already exists')



# class EmployeeEditForm(forms.ModelForm):
# 	def __init__(self, *args, **kwargs):
# 		qual_CHOICES=(('B.Sc','B.Sc',),('M.Sc','M.Sc',),('BTech','BTech',),('MTech','MTech',),('MCA','MCA',),('MBA','MBA',),('BBA','BBA',),('BCA','BCA',))
# 		super(EmployeeEditForm, self).__init__(*args, **kwargs)
# 		self.fields['dept'].choices = [(dept.id, str(dept.name)) for dept in Department.objects.all()]
# 		self.fields['qualification'].choices = qual_CHOICES
# 		self.fields['mobile_no'].required = True
# 		self.fields['dob'].required = True

# 	qualification = forms.MultipleChoiceField(required=True,widget=forms.SelectMultiple(attrs={'class': 'selectpicker','data-selected-text-format':'count'}))
# 	dept = forms.ChoiceField(widget=Select(attrs={'class': 'selectpicker', 'style': 'width:95%'}))
# 	class Meta:
# 		model=Employee
# 		widgets={
# 			'first_name':forms.TextInput(attrs={'class': 'form-control'}),
# 			'last_name':forms.TextInput(attrs={'class': 'form-control'}),
# 			'address':forms.Textarea(attrs={'class': 'form-control'}),
#         	'dob':forms.TextInput(attrs={'class': 'form-control datepicker', 'id': 'dob', 'required': 'required', 'placeholder': 'YYYY-MM-DD'}),
# 			'mobile_no':forms.TextInput(attrs={'class': 'form-control'}),
# 			# 'mobile_no' = forms.TextInput(attrs={'placeholder': 'Type your mobileno', 'class': 'form-control'},required=True),
# 			# email=forms.EmailField(label='Email',required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Your e-mail ID', 'class': 'form-control  ','id':'ind_email','required':'required','maxlength' : '50'}))
# 			# 'dept' = forms.Select(attrs={'class': 'selectpicker','data-selected-text-format':'count'})
# 		}

# 	def clean_first_name(self):
# 		if re.match(r"^[a-zA-Z. ]*$", self.cleaned_data['first_name'].strip()):
# 			return self.cleaned_data['first_name'].strip()
# 		raise forms.ValidationError('Enter Alphabets only')

# 	def clean_last_name(self):
# 		if re.match(r"^[a-zA-Z0-9. ]*$", self.cleaned_data['last_name'].strip()):
# 			return self.cleaned_data['last_name'].strip()
# 		raise forms.ValidationError('Enter Alphabets only')

# 	def clean_mobile_no(self):
# 		if re.match(r"^([0-9+(). -]{6,12})$", self.cleaned_data['mobile_no'].strip()):
# 			if len(self.cleaned_data['mobile_no']) < 10:
# 				raise forms.ValidationError('Phone Number must contain at least eight digits')
# 			return self.cleaned_data['mobile_no'].strip()
# 		raise forms.ValidationError('Invalid Mobile No.')

	# def clean_email(self):
	# 	if User.objects.filter(email__exact=self.cleaned_data['email']).count()>0:
	# 		raise forms.ValidationError('e-mail ID already exists')

class LeaveRequestForm(forms.Form):
	def __init__(self, *args, **kwargs):
		# dept_CHOICES=(('Human Resource','Human Resource',),('Software Development','Software Development',),('Documentation','Documentation'),('Testing','Testing',))
		# qual_CHOICES=(('B.Sc','B.Sc',),('M.Sc','M.Sc',),('BTech','BTech',),('MTech','MTech',),('MCA','MCA',),('MBA','MBA',),('BBA','BBA',),('BCA','BCA',))
		super(LeaveRequestForm, self).__init__(*args, **kwargs)
		# self.fields['qualification'].choices = qual_CHOICES
		self.fields['ltype'].choices = [(lt.id, str(lt.ltype)) for lt in LeaveType.objects.all()]
		# self.fields['emp'].choices = [(emp.id, str(emp.usr.first_name)) for emp in Employee.objects.all()]

	# emp = forms.ChoiceField(required=True,widget=forms.Select(attrs={'class': 'selectpicker','data-selected-text-format':'count'}))
	leave_from  =  forms.CharField(label='Leave from',widget=forms.TextInput(attrs={'class': 'form-control datepicker','id':'leave_from','required':'required','placeholder':'YYYY-MM-DD','readonly':'true'}))
	leave_to =  forms.CharField(label='Leave to',widget=forms.TextInput(attrs={'class': 'form-control datepicker','id':'leave_to','required':'required','placeholder':'YYYY-MM-DD','readonly':'true'}))
	no_of_days = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','readonly':'true'}),required=True)
	# ltype = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)

	ltype = forms.ChoiceField(required=True,widget=forms.Select(attrs={'class': 'selectpicker','data-selected-text-format':'count'}))
	reason = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Reason for Leave', 'class': 'form-control'}))
    # exclude = ['created_on', 'updated_on', 'status', 'size']

    
class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your username', 'class': 'form-control','id':'log_uname'}),required=True)
	pwd = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control ','id':'log_pwd'}),required=True)

class LeaveTypeForm(forms.ModelForm):
	class Meta:
		model=LeaveType
		widgets={
		 'ltype': forms.TextInput(attrs={'class': 'form-control'})
		}

	
	def clean_ltype(self):
		if LeaveType.objects.filter(ltype__exact=self.cleaned_data['ltype']).count() > 0:
			raise forms.ValidationError('This Type already exists')
		return self.cleaned_data['ltype']

class AssignEmpHeadForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(AssignEmpHeadForm, self).__init__(*args, **kwargs)
		self.fields['department'].choices = [(dept.id, str(dept.name)) for dept in Department.objects.all()]
		self.fields['employee'].choices = [(emp.id, str(emp.usr.first_name)) for emp in Employee.objects.all()]

	department = forms.ChoiceField(required=True,widget=forms.Select(attrs={'class': 'selectpicker','id':'dept','data-selected-text-format':'count'}))
	employee = forms.ChoiceField(required=True,widget=forms.Select(attrs={'class': 'selectpicker','id':'emp','data-selected-text-format':'count'}))

	def clean_department(self):
		if self.cleaned_data['department']:
			return self.cleaned_data['department']
		else:
			raise forms.ValidationError('Must select a department')
	def clean_employee(self):
		if self.cleaned_data['employee']:
			return self.cleaned_data['employee']
		else:
			raise forms.ValidationError('Must select a employee')




