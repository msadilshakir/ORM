from django.shortcuts import render, redirect ,HttpResponse
from .models import order, transaction
import random
from django.db import connection

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
        payment_type=request.POST['payment_type']
        #email=request.POST['email']
        transaction_status = random.randrange(2)
        obj = order.objects.latest('id')
        email = order.objects.get(id=obj.id).email
        s=transaction(payment_type=payment_type,order_id=obj.id,transaction_status=transaction_status)
        s.save()
        print("Submitted")
        return render(request,'base.html',{'obj':email})

def ordertable(request):
    ord_tb=order.objects.all()
    return render(request,'ordertable.html',{'ord_tb':ord_tb})


def transactiontable(request):
    trans_tb=transaction.objects.all()
    return render(request,'transactiontable.html',{'trans_tb':trans_tb})


def tablejoin(request):
    cursor=connection.cursor()
    cursor.execute("select prac_order.first_name as first,prac_transaction.order_id,prac_transaction.transaction_status,prac_transaction.payment_type from prac_order join prac_transaction on prac_order.id=prac_transaction.order_id")
    results=cursor.fetchall()
    print(results)
    return render(request,'order_status.html',{'results':results})