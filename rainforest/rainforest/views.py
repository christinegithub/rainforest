from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rainforest.models import Product


def root(request):
    return HttpResponseRedirect('/home')

def home_page(request):
    context = {'products': Product.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def product_show(request, id):
    product = Product.objects.get(pk=id)
    context = {'product': product}
    response = render(request, 'product.html', context)
    return HttpResponse(response)
