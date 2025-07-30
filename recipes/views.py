from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Nicolas'
    })

def about(request):
    return render(request)

def contact(request):
    return render(request, 'recipes/contato.html')