from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello world")
    return render(request, 'home.html', {'name':'Amar'})

def add(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']
    res = int(num1) + int(num2)
    return render(request, 'result.html', {'res': res})
