from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("<H1>Hello World <br> This is My World Wide Web </H1>")

def home(request):
    return render(request, 'home.html')

def firstweb(request):
    return render(request, 'firstweb.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def thirdpage(request):
    return render(request, 'thirdpage.html')

def hny(request):
    return render(request, 'hny.html')
