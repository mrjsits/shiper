from django.db import models
from django.utils import timezone
import  random
# Create your models here.

class Info(models.Model):
	name = models.CharField(max_length=120, default = "Tên người gửi")
	address = models.CharField(max_length=120, default = "Địa chỉ người gửi")
	phone = models.CharField(max_length = 80, default = "Số điện thoại người gửi")
	reciever = models.CharField(max_length=120, default = "Tên người nhận")
	reciever_address = models.CharField(max_length=120, default = "Địa chỉ người nhận")
	reciever_phone = models.CharField(max_length=80, default = "Số điện thoại người nhận")
	shipcode = models.CharField(max_length=80)
	created = models.DateTimeField(default=timezone.now(), editable = False)
	status = models.BooleanField(default = False)
	body = models.TextField(default = "Nội dung")
	
	def sender(self):
		return self


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
