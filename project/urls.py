"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tiko.views import ProductsList, ProductsDetailView, ProductCreateView
from tiko import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', ProductsList.as_view(), name='main'),
    path('main/<int:pk>/', ProductsDetailView.as_view(), name = 'detail'),
    path('main/save/', ProductCreateView.as_view(), name = 'save'),
    #path('main/del/', views.delprod, name = 'del'),
    path('main/update', views.updateprod, name = 'update'),
]
