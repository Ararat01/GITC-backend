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
from tiko.views import ProductsList, ProductsDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView, LogIn, logout_user, RegisterUser
from tiko import views
from project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', ProductsList.as_view(), name='main'),
    path('main/<int:pk>/', ProductsDetailView.as_view(), name = 'detail'),
    path('main/save/', ProductCreateView.as_view(), name = 'save'),
    path('main/<int:pk>/del/', ProductDeleteView.as_view(), name = 'del'),
    path('main/<int:pk>/update/', ProductUpdateView.as_view(), name = 'update'),
    path('main/login/', LogIn.as_view(), name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('register/', RegisterUser.as_view(), name = 'register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)