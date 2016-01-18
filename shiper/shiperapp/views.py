from django.shortcuts import render, redirect
from .models import Info, StoreCode, Profile
from .forms import Order, Shipcode, Moveback, Showorder, Register, Login, UserOrder, Logout
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def order_detail(request, pk):
	post = get_object_or_404(Info, pk=pk)
	if request.method == "POST":
		return redirect('order_edit', pk=post.pk)
	else:
		post = get_object_or_404(Info, pk=pk)
		return render(request, 'orderdetail.html', {'post': post})

#if request.user.is_authenticated():
    # Do something for authenticated users.
#else:
    # Do something for anonymous users.

@login_required
def order_new (request):
	if request.method == "POST":
		code = Shipcode(request.POST)
		form = Order(request.POST)
		logouts = Logout(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			post.createcode()
			return redirect('order_detail', pk=post.pk)
		elif code.is_valid():
			cc = code.save(commit=False) # because form Shipcode don't have attribute shipcode
			found = Info.objects.get(shipcode=cc.getcode())	
			return redirect('order_detail', pk=found.pk)
		elif logouts.is_valid():
			logout(request)	
			return redirect('loginview')
	if request.user.is_authenticated():
		form = Order()
		logouts = Logout()
		return render(request, 'order.html', {'form': form, 'logouts': logouts})
	#return redirect('loginview')

def order_edit(request, pk):
	order = get_object_or_404(Info, pk=pk)
	form = Order(instance = order)
	moveback = Moveback()
	max_pk = 0
	info = Info.objects.all()
	for i in info:
		max_pk = max(max_pk, int(i.pk))
	if request.method == "POST":
		keep = Order(request.POST)	
		if keep.is_valid():
			Info.objects.filter(pk=pk).delete()	
			post = keep.save(commit = False)
			post.createcode()
			post.save()
			form = Order(instance = post)
			render(request, 'orderedit.html', {'form':form})
			return redirect('order_edit', pk=str(int(max_pk)+1))
		else:
			return redirect('order_detail', pk=pk)
	else:
		return render(request, 'orderedit.html', {'form':form, 'moveback': moveback})

def order_show(request):
	list_order = Info.objects.all()
	return render(request, 'ordershow.html', {'list_order':list_order})

def registerview(request):
	registerform = Register()
	if request.method == "POST":
		recieveform = Register(request.POST)
		if recieveform.is_valid():
			data = recieveform.save(commit = False)
			if data.password == data.repeat_password:
				try:
					user = User.objects.create_user(request.POST['username'],' ',request.POST['password'])
					user.save()
					user.has_perm('foo.add_bar')
					user.has_perm('foo.change_bar')
					user.has_perm('foo.delete_bar')	
					data.save()
					form = Order()
					code = Shipcode()
					return redirect( 'order_new')
				except:
					pass
	registerform = Register()
	return render(request, 'register.html', {'registerform': registerform})


def loginview (request):
	loginform = Login()
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('order_new')
	return render(request, 'login.html', {'loginform': loginform})

