from django.shortcuts import render #, render_to_response
#from django.core.context_processors import csrf

from .models import Products
from .forms import ProductForm

# Create your views here.

def product_form_view(request):
    print(request.POST['title'])
    print(request.POST)
    context = {}
    return render(request, "product/product_create.html", context)
# def product_form_view(request):
#     form = ProductForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)
    


def product_detail_view(request):
    obj = Products.objects.get(id=1)
    #context = {
    #    'title': obj.title,
    #    'description': obj.description,
    #    'price': obj.price,
    #    'summary': obj.summary
    #}
    context = {
        'object': obj
    }
    return render(request, "product/product_detail.html", context)