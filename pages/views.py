# from django.shortcuts import render
# from django.http import HttpResponse

# from .models import product_info
# from .forms import product_info_form 

# # Create your views here.
# def personal_info_view(request):
#     form = product_info_form(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form.product_info_form()

#     context = {
#         'form': form
#     }
#     return render(request, "home.html", context)

# # def contact_view(request):
# #     return "Contact zone"

# # def about_view(request):
# #     return "About us"
# #def contact_view(request, *args, **kwargs):
# #    my_context = {
#  #       "name": "tom will be a manager",
#   #      "my_number": "123-444-5267",
#    #     "my_list": [123, 456, 789,'ibm'],
#     #    "my_html": "<h1>I used safe filter here</h1>"
#     #}
#     #return render(request, "contact.html", my_context)

# #def about_view(request, *args, **kwargs):
#  #   return render(request, "about.html", {})
