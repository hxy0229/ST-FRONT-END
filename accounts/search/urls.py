from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url('searchCustomerByUEN', views.searchCustomerByUEN, name='searchCustomerByUEN'),
    url('searchCustomerByName', views.searchCustomerByName, name='searchCustomerByName'),
    url('searchProduct', views.searchProduct, name='searchProduct'),
]
