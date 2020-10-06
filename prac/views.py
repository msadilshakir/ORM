from django.shortcuts import render, redirect ,HttpResponse
from .models import order, transaction

# Create your views here.

def base(request):
    return render(request,'base.html')

def order1(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        s=order(first_name=first_name,last_name=last_name,email=email,password=password)
        s.save()
        return render(request,'transaction.html')
    return render(request,'order.html')


def transaction1(request):
    if request.method == 'POST':
        name=request.POST['name']
        #email=request.POST['email']
        obj = order.objects.latest('id')
        email = order.objects.get(id=obj.id).email
        s=transaction(name=name,email=email,order_id=obj.id)
        s.save()
        print("Submitted")
        return render(request,'base.html',{'obj':email})

def ordertable(request):
    ord_tb=order.objects.all()
    return render(request,'ordertable.html',{'ord_tb':ord_tb})


def transactiontable(request):
    trans_tb=transaction.objects.all()
    return render(request,'transactiontable.html',{'trans_tb':trans_tb})


