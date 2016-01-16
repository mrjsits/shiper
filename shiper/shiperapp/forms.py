from .models import Info, StoreCode
from django import forms

class Order(forms.ModelForm):
	class Meta:
		model = Info
		fields = ['name', 'address','phone','reciever','reciever_address','reciever_phone','body']

class Shipcode(forms.ModelForm):
	class Meta:
		model = StoreCode
		fields = ['shipcode']


			
