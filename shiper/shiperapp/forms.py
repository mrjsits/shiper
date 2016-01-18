from .models import Info, StoreCode, Profile
from django import forms
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
class Order(forms.ModelForm):
	class Meta:
		model = Info
		fields = ['reciever','reciever_address','reciever_phone','body']

class Shipcode(forms.ModelForm):
	class Meta:
		model = StoreCode
		fields = ['shipcode']

class Moveback(forms.ModelForm):
	class Meta:
		model = StoreCode
		fields = []

class Showorder(forms.ModelForm):
	class Meta:
		model = Info
		fields =  ['reciever_address', 'reciever_phone', 'status', 'created', 'shipcode' ]

class Register(forms.ModelForm):
	password = forms.CharField(max_length = 120, widget = forms.PasswordInput())
	repeat_password = forms.CharField(max_length = 120, widget = forms.PasswordInput())
	class Meta: 
		model =  Profile
		fields = ['fullname','username','password', 'repeat_password', 'address', 'phone', 'captcha']

class Login(forms.ModelForm):
	password = forms.CharField(max_length = 120, widget = forms.PasswordInput())
	class Meta:
		model = Profile
		fields = ['username', 'password']

class UserOrder(forms.ModelForm):
	class Meta:
		model = Info
		fields = ['reciever','reciever_address','reciever_phone','body']

class Logout(forms.ModelForm):
	class Meta:
		model = User
		fields = []