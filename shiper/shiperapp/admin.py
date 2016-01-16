from django.contrib import admin
from .models import Info
# Register your models here.

class ControlAdmin(admin.ModelAdmin):
	list_display =['name','phone','reciever','reciever_phone','created', 'status']
	class Meta:
		models = Info
admin.site.register(Info, ControlAdmin)