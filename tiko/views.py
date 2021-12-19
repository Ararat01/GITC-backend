from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView


class ProductsList(ListView):
    model = Product
    context_object_name = 'latest_products_list'
    template_name = 'list.html'

class ProductsDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'detail.html'

class ProductCreateView(CreateView):
    fields = ('name', 'product_info', 'product_price', 'image')
    model = Product
    template_name = 'save.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.FILES)
        return super().post(request, *args, **kwargs)
    
    def get_success_url(self, **kwargs):
        return reverse('detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'list.html'
    success_url = reverse_lazy('main')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'product_info', 'product_price')
    template_name = 'update.html'

    def get_success_url(self, **kwargs):
        return reverse('detail', kwargs={'pk': self.object.pk})


class LogIn(LoginView):
    template_name = 'login.html'