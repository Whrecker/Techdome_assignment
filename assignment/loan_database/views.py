from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Customers,Admin
import json
from django.core.serializers.json import DjangoJSONEncoder
import datetime
from rest_framework import generics
from .serializer import CustomerSerializer
from django.http import JsonResponse

# Create your views here.
class CustomerMake(generics.ListCreateAPIView):
	queryset=Customers.objects.all()
	serializer_class=CustomerSerializer
class CustomerDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset=Customers.objects.all()
	serializer_class=CustomerSerializer
	lookup_field="pk"
def home(request):
	if request.method=="POST":
		selected_role = request.POST.get('selected')
		if selected_role=="Customer":
			return redirect("login")
		if selected_role=="Admin":
			return redirect("login_admin")
	return render(request,'assignment/home.html')
def login(request):
	data=Customers.objects.all()
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		if data:
			for i in data:
				flag=0
				if username == i.username:
					flag=1
					if username==i.username and password==i.password:
						print(i.username)
						return redirect("customer",pk=i.ids)
			if flag==0:
				user_credentials = Customers(username=username, password=password,loan_taken=0,loan_remaining=0,repayment_time=None,loan_status="Pending",loan_term=None)
				user_credentials.save()
				return redirect("customer",pk=i.ids+1)			
		else:
			user_credentials = Customers(username=username, password=password,loan_taken=0,loan_remaining=0,repayment_time=None,loan_status="Pending",loan_term=None)
			user_credentials.save()
			return redirect("customer",pk=1)
	return render(request,'assignment/login.html')
def login_admin(request):
	data=Admin.objects.all()
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		if data:
			for i in data:
				if username == i.name:
					if username==i.name and password==i.password:
						print(i.name)
						return redirect("admin",pk=i.ids)
	return render(request,'assignment/login_admin.html')



def customer(request, pk):
	data = Customers.objects.get(ids=pk)
	if request.method == "POST":
		amount = request.POST.get("amount")
		pay = request.POST.get("pay")
		loan_term=request.POST.get("term")
		if not amount:
			loan_taken = data.loan_taken
		else:
			loan_taken = data.loan_taken + int(amount)
		if pay:
			loan_remaining = data.loan_remaining-int(pay)
		else:
			if loan_taken!=0 and data.loan_remaining>0:
				loan_remaining = loan_taken-data.loan_remaining
			elif loan_taken!=0 and data.loan_remaining==0:
				loan_remaining=loan_taken
			else:
				loan_remaining=0
		if loan_remaining!=0:
			Customers.objects.filter(pk=data.ids).update(
				loan_taken=loan_taken,
				loan_remaining=loan_remaining,
				repayment_time=datetime.datetime.now()+datetime.timedelta(days=7),
				loan_term=loan_term
				)
		else:
			Customers.objects.filter(pk=data.ids).update(
				loan_taken=loan_taken,
				loan_remaining=loan_remaining,
				repayment_time=datetime.datetime.now()+datetime.timedelta(days=7),
				loan_status="Paid",
				loan_term=loan_term
				)
		return redirect("customer",pk=data.ids)
	data = Customers.objects.get(ids=pk)
	if data.repayment_time:
		return render(request, 'assignment/customer.html', {
			'repayment_time': data.repayment_time.strftime('%Y-%m-%d %H:%M:%S'),
			'loan_term':data.loan_term,
			'loan_remaining': json.dumps(data.loan_remaining),
			})
	else:
		return render(request, 'assignment/customer.html', {
			'repayment_time': None,
			'loan_term':None,
			'loan_remaining': json.dumps(data.loan_remaining),
			})

def admin(request,pk):
	data=Customers.objects.all()
	if request.method == 'POST':
		id=request.POST.get("approve")
		Customer.objects.filter(pk=id).update(loan_status="approve")
		return redirect("admin.html")
	return render(request,'assignment/admin.html',{'data':data})
def approve(request):
    if request.method == "POST":
        id = request.POST.get("row_Id")
        print(id)
        Customers.objects.filter(pk=id).update(loan_status="approve")
        return JsonResponse({'message': 'Loan approved successfully'})  # Return a JSON response
    return HttpResponse("approve")




