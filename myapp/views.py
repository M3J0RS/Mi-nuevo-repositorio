from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def servicios(request):
    return render(request, 'servicios.html')

def facturas(request):
    return render(request, 'facturas.html')

