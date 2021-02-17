from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from testapp.models import Company,Employee

# Create your views here.
class Companylistview(ListView):
    model=Company
class Companydetailview(DetailView):
    model=Company
class Companycreateview(CreateView):
    model=Company
    fields=('cname','location','ceo')
class Employeecreateview(CreateView):
    model=Employee
    fields=('eno','ename','esal','company')
