from django.contrib import admin
from .models import Customer, Asset, Misc

# Register your models here.
class CustomerList(admin.ModelAdmin):
    list_display = ('cust_number', 'name', 'city', 'cell_phone')
    list_filter = ('cust_number', 'name', 'city')
    search_fields = ('cust_number', 'name')
    ordering = ['cust_number']

class AssetList(admin.ModelAdmin):
    list_display = ('customer', 'category', 'description', 'value')
    list_filter = ('customer', 'category')
    search_fields = ('customer', 'category')
    ordering = ['customer']

class MiscList(admin.ModelAdmin):
    list_display = ('customer', 'name', 'value')
    list_filter = ('customer', 'name')
    search_fields = ('customer', 'name')
    ordering = ['customer']


admin.site.register(Customer, CustomerList)
admin.site.register(Asset, AssetList)
admin.site.register(Misc, MiscList)



