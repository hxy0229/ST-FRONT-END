from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.input, name='input'),
    #path('inputNewDeal/', views.inputNewDeal, name='inputNewDeal'),
#    url(r'^searchCustomerByName/$', views.searchByCustomerName),
#    url(r'^searchCustomerByUEN/$', views.searchByUEN),
#    url(r'^createCustomer/$', views.createCustomer),
#    url(r'^inputDeals/$',views.inputDeals, views.inputDeals),
]
