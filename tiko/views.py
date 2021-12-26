from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from .models import Product
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from tiko.forms import UserSignupForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

class UserCheckerMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse(status=403)

class ProductsList(ListView):
    model = Product
    context_object_name = 'latest_products_list'
    template_name = 'list.html'

class ProductsDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    fields = ('name', 'product_info', 'product_price', 'image')
    model = Product
    template_name = 'save.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.get_success_url())
    
    def get_success_url(self, **kwargs):
        return reverse('detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, UserCheckerMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Product
    template_name = 'list.html'
    success_url = reverse_lazy('main')

    

class ProductUpdateView(LoginRequiredMixin, UserCheckerMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Product
    fields = ('name', 'product_info', 'product_price')
    template_name = 'update.html'

    def get_success_url(self, **kwargs):
        return reverse('detail', kwargs={'pk': self.object.pk})


class LogIn(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('main') settings.py login_rederict

def logout_user(request):
    logout(request)
    return redirect(reverse('login'))

class RegisterUser(FormView):
    form_class = UserSignupForm
    template_name = 'register.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = get_user_model()()
        user.username = form.cleaned_data['username']
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)
