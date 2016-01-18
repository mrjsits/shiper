from django.db import models
from django.utils import timezone
import  random
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your models here.

class Info(models.Model):
	username = models.CharField(max_length=120)
	reciever = models.CharField(max_length=120, default = "Tên người nhận")
	reciever_address = models.CharField(max_length=120, default = "Địa chỉ người nhận")
	reciever_phone = models.CharField(max_length=80, default = "Số điện thoại người nhận")
	shipcode = models.CharField(max_length=80)
	created = models.DateTimeField(default=timezone.now(), editable = True)
	status = models.BooleanField(default = False)
	body = models.TextField(default = "Nội dung")

	def createcode(self):
 		info = Info.objects.all()
 		l_max = 8
 		temp = ''
 		for i in range(0,l_max):
 			temp += random.choice('0123456789abcdefghijklmnopqrstuxyzABCDEFGHIJKLMNOPQRSTUXYZ')
 		while True:
 			found = False
 			for i in info:
 				if i.shipcode == temp:
 					found = True
 					break

 			if found:
 				temp = ''
 				for i in l_max:
 					temp += random.choice('0123456789abcdefghijklmnopqrstuxyzABCDEFGHIJKLMNOPQRSTUXYZ')
 			else:
 				self.shipcode = temp
 				self.save()
 				break


class StoreCode(models.Model):
	shipcode = models.CharField(max_length=80)
	def  getcode(self):
		return str(self.shipcode)


#ForeignKey('username', on_delete = models.CASCADE)
class Profile (models.Model):
	fullname = models.CharField(max_length = 120)
	username = models.CharField(max_length = 120)
	password = models.CharField(max_length = 120)
	repeat_password = models.CharField(max_length = 120)
	address = models.CharField(max_length = 120)
	phone = models.CharField(max_length = 120)
	captcha = models.CharField(max_length = 120)
	created = models.DateTimeField(default=timezone.now(), editable = False)
	def createcode(self):
 		l_max = 8
 		temp = ''
 		for i in range(0,l_max):
 			temp += random.choice('0123456789abcdefghijklmnopqrstuxyzABCDEFGHIJKLMNOPQRSTUXYZ')
 			self.captcha = temp
 			self.save()