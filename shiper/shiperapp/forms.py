from .models import Info, StoreCode
from django import forms
from django.views.generic.edit import UpdateView
class Order(forms.ModelForm):
	class Meta:
		model = Info
		fields = ['name', 'address','phone','reciever','reciever_address','reciever_phone','body']
	

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
		fields =  ['name', 'address', 'phone', 'reciever', 'reciever_address', 'reciever_phone', 'status', 'created', 'shipcode' ]