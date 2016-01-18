from django.contrib import admin
from .models import Info, Profile
from django.contrib.auth.models import User
# Register your models here.

class ControlAdmin(admin.ModelAdmin):
	list_display =['reciever','reciever_phone','created', 'status']
	class Meta:
		models = Info
admin.site.register(Info, ControlAdmin)

class ListRegister(admin.ModelAdmin):
	list_display = ['username', 'password', 'address', 'phone', 'created']
	class Meta:
		models = Profile
admin.site.register(Profile, ListRegister)

class ViewUser(admin.ModelAdmin):
	list_display = ['username', 'password']
	class Meta:
		models = User
