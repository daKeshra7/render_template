"""newblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from pages.views import personal_info_view, contact_view, about_view
from  product.views import product_detail_view, product_form_view,lookup_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('contact', contact_view),
    # path('about', about_view, name="about"),
    # path('product/', product_detail_view),
    # path('create/', product_form_view)
    path('product/<int:my_id>', lookup_view, name='product')
]
