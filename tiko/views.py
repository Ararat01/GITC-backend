from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductsList(ListView):
    model = Product
    context_object_name = 'latest_products_list'
    template_name = 'list.html'

class ProductsDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'detail.html'

# def detail(request, **kwargs):
#     product_id = kwargs['pk']
#     try:
#         a = Product.objects.get( id = product_id )
#     except:
#         raise Http404("Can't found a product")

#     return render(request, 'detail.html', {'product': a})

class ProductCreateView(CreateView):
    #model = Product
    fields = ('name', 'product_info', 'product_price')
    model = Product
    template_name = 'save.html'
    
    def get_success_url(self, **kwargs):
        return reverse('detail', kwargs={'pk': self.object.pk})

# def saveprod(request):
#     if request.method == 'POST':    
#         a = Product(name = request.POST['name'], product_info = request.POST['info'], product_price = request.POST['price'])
#         a.save()
#         return HttpResponseRedirect(reverse(detail, kwargs={'pk': a.pk}))

# class ProductDeleteView(DeleteView):
#     model = Product
#     success_url = reverse_lazy('main')


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