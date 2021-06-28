from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")
    # return HttpResponse("hello!")
    # render an entire HTML file
    # render a template: hello/DjangoProject/hello/template/hello/index.html
    # second argument?

# HTTPResponse is a special class created by Django
# if you want use it, import it.


def brain(request):
    return HttpResponse("hello, Brain!")


def david(request):
    return HttpResponse("hello, David")


# def greet(requset, name):
#     return HttpResponse(f"hello,{name.capitalize()}")
    # 首字母大写 take the name capitalize it
    # and I have now been add to a route that takes an HTTP request as well as parameter,
    # --that name, whatever was in the URL and return HTTP response that just says hello
    # to that person.So these HTTP responses can be any HTML content, right now text, you can
    # adding lists or tables to this as well.

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})
