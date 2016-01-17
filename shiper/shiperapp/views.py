from django.shortcuts import render, redirect
from .models import Info, StoreCode
from .forms import Order, Shipcode, Moveback, Showorder
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.


def order_detail(request, pk):
	post = get_object_or_404(Info, pk=pk)
	if request.method == "POST":
		return redirect('order_edit', pk=post.pk)
	else:
		post = get_object_or_404(Info, pk=pk)
		return render(request, 'orderdetail.html', {'post': post})


def order_new (request):
	if request.method == "POST":
		code = Shipcode(request.POST)
		form = Order(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			post.createcode()
			return redirect('order_detail', pk=post.pk)
		elif code.is_valid():
			cc = code.save(commit=False) # because form Shipcode don't have attribute shipcode
			found = Info.objects.get(shipcode=cc.getcode())	
			return redirect('order_detail', pk=found.pk)
	form = Order()
	code = Shipcode()
	return render(request, 'order.html', {'form': form, 'code': code})

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