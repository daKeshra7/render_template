from django.shortcuts import render #, render_to_response
#from django.core.context_processors import csrf


from .models import Products
# from .forms import ProductForm,  RawProductForm


# Create your views here.

def lookup_view(request, my_id):
    obj = Products.objects.get(id=my_id)
    context = {
        'object':obj
    }
    
    return render(request, 'product/product_create.html', context)

def product_form_view(request):
    initial_data = {
        'first_name': 'Bolanle'
    }
    obj = Products.objects.get(id=2)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


# def product_form_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Products.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()
#         else:
#             print(my_form.errors)
        
#     context = {
#         'form': my_form
#     }
#     return render(request, "product/product_create.html", context)




# def product_form_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST )
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Products.objects.create(**my_form.cleaned_data)
#             form.save()

#         else:
#             print(my_form.errors)
     
#     context = {
#         'form': my_form
#     }
#     return render(request, "product/product_create.html", context)

# # def product_form_view(request):
#     # print(request.POST['title'])
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = {}
#     return render(request, "product/product_create.html", context)
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