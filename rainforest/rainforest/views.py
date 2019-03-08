from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rainforest.models import Product

def home_page(request):
    context = {'products': Product.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
