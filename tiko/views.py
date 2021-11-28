from django.http import Http404, HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductsList(ListView):
    model = Product
    context_object_name = 'latest_products_list'
    template_name = 'list.html'


class ProductsDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'detail.html'

    
class ProductCreateView(CreateView):
    fields = ('name', 'product_info', 'product_price')
    model = Product
    tamplate_name = 'save.html'

def delprod(request):
    if request.method == 'POST':    
        Product.objects.get( id = request.POST['id']).delete()
        return HttpResponseRedirect(reverse(main))


def updateprod(request):
    if request.method == 'POST':
        myProd = Product.objects.get( id = request.POST['id'])
        myProd.name = request.POST['name']
        myProd.product_info = request.POST['info']
        myProd.product_price = request.POST['price']
        myProd.save()
        return HttpResponseRedirect(reverse(main))

def back(request):
    return HttpResponseRedirect(reverse(main))