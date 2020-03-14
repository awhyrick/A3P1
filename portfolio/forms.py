from django import forms
from .models import Customer, Misc, Asset

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)

class MiscForm(forms.ModelForm):
   class Meta:
       model = Misc
       fields = ('customer', 'make', 'model', 'name', 'value', 'category', 'description', 'date',)

class AssetForm(forms.ModelForm):
   class Meta:
       model = Asset
       fields = ('customer', 'make', 'model', 'serial_number', 'category', 'description', 'value', 'date',)