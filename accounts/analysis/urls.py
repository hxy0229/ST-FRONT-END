from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.analysis, name='analysis'),
    url(r'^$', views.analyzeCustomer, name='analysis'),
    url('findProductForCustomerAnalysis', views.findProductForCustomerAnalysis, name='findProductForCustomerAnalysis'),
url('findProductForCustomerNameAnalysis', views.findProductForCustomerNameAnalysis, name='findProductForCustomerNameAnalysis'),
    url('customerProductMatchAnalysis', views.customerProductMatchAnalysis, name='customerProductMatchAnalysis'),
    url('findCustomerForProductAnalysis', views.findCustomerForProductAnalysis, name='findCustomerForProductAnalysis'),
]
