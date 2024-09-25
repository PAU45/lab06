from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def facturas(request):
    return HttpResponse("factura_form")