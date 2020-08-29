from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html",  {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "name": "tom will be a manager",
        "my_number": "123-444-5267",
        "my_list": [123, 456, 789,'ibm'],
        "my_html": "<h1>I used safe filter here</h1>"
    }
    return render(request, "contact.html", my_context)

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})
