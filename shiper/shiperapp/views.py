from django.shortcuts import render, redirect
from .models import Info, StoreCode
from .forms import Order, Shipcode
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.


def order_detail(request, pk):
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
		else:	
			form = Order()
			return render(request, 'order.html', {'form': form, 'code': code})
	else:
		form = Order()
		code = Shipcode()
		return render(request, 'order.html', {'form': form, 'code': code})
