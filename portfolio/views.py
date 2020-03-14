from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer


# Create your views here.
now = timezone.now()
def home(request):
   return render(request, 'portfolio/home.html',
                 {'portfolio': home})

@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/customer_list.html',
                 {'customers': customer})

@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/customer_list.html',
                         {'customers': customer})
   else:
        # edit
       form = CustomerForm(instance=customer)
   return render(request, 'portfolio/customer_edit.html', {'form': form})

@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('portfolio:customer_list')

@login_required
def misc_list(request):
   miscs = misc.objects.filter(created_date__lte=timezone.now())
   return render(request, 'portfolio/misc_list.html', {'miscs': miscs})

@login_required
def misc_new(request):
   if request.method == "POST":
       form = MiscForm(request.POST)
       if form.is_valid():
           misc = form.save(commit=False)
           misc.created_date = timezone.now()
           misc.save()
           misc = misc.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/misc_list.html',
                         {'miscs': misc})
   else:
       form = MiscForm()
       # print("Else")
   return render(request, 'portfolio/misc_new.html', {'form': form})

@login_required
def misc_edit(request, pk):
   misc = get_object_or_404(Misc, pk=pk)
   if request.method == "POST":
       form = MiscForm(request.POST, instance=misc)
       if form.is_valid():
           misc = form.save()
           misc.updated_date = timezone.now()
           misc.save()
           misc = misc.objects.filter(date=timezone.now())
           return render(request, 'portfolio/misc_list.html', {'misc': misc})
   else:
       # print("else")
       form = MiscForm(instance=misc)
   return render(request, 'portfolio/misc_edit.html', {'form': form})

@login_required
def misc_delete(request, pk):
   misc = get_object_or_404(Misc, pk=pk)
   misc.delete()
   return redirect('portfolio:misc_list')

@login_required
def asset_list(request):
    asset = asset.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/asset_list.html',
                 {'assets': asset})

@login_required
def asset_new(request):
   if request.method == "POST":
       form = assetForm(request.POST)
       if form.is_valid():
           asset = form.save(commit=False)
           asset.created_date = timezone.now()
           asset.save()
           asset = asset.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/asset_list.html',
                         {'assets': asset})
   else:
       form = assetForm()
       # print("Else")
   return render(request, 'portfolio/asset_new.html', {'form': form})

@login_required
def asset_edit(request, pk):
    asset = get_object_or_404(asset, pk=pk)
    if request.method == "POST":
       form = assetForm(request.POST, instance=asset)
       if form.is_valid():
           asset = form.save()
           asset.updated_date = timezone.now()
           asset.save()
           asset = asset.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/asset_list.html', {'assets': asset})
    else:
       # print("else")
       form = assetForm(instance=asset)
    return render(request, 'portfolio/asset_edit.html', {'form': form})

@login_required
def asset_delete(request, pk):
   asset = get_object_or_404(asset, pk=pk)
   asset.delete()
   return redirect('portfolio:asset_list')

class CustomerList(APIView):

    def get(self,request):
        customers_json = Customer.objects.all()
        serializer = CustomerSerializer(customers_json, many=True)
        return Response(serializer.data)

