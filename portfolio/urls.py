from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('misc_list', views.misc_list, name='misc_list'),
    path('misc/create/', views.misc_new, name='misc_new'),
    path('misc/<int:pk>/edit/', views.misc_edit, name='misc_edit'),
    path('misc/<int:pk>/delete/', views.misc_delete, name='misc_delete'),
    path('asset_list', views.asset_list, name='asset_list'),
    path('asset/create/', views.asset_new, name='asset_new'),
    path('asset/<int:pk>/edit/', views.asset_edit, name='asset_edit'),
    path('asset/<int:pk>/delete/', views.asset_delete, name='asset_delete'),
    url(r'^customers_json/', views.CustomerList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
