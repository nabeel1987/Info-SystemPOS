from django.http import HttpResponse


from django.template import loader
from .models import Laptop,Mobile,Book
from django.http import Http404
from django.shortcuts import get_object_or_404,render
# Create your views here.

def index(request):
    latest_mobile_list=Mobile.objects.order_by('Price')[:5]
    context={'latest_mobile_list':latest_mobile_list,}
    my_path='Inventory/index.html'
    return render(request,my_path,context)

def detail(request,Name_id):
    mobile=get_object_or_404(Mobile, pk=Name_id) #this is the context variable: mobile which will be used in details.html
    return render(request,'Inventory/detail.html', {'mobile':mobile})

def results(request,Name_id):
    return HttpResponse("You are looking at the result %s" % Name_id)

def display_laptop(request,Laptop_id):
    items=get_object_or_404(Laptop,pk=Laptop_id)
    context={
        'items':items,
    }
    return render(request,'Inventory/index.html',context)
