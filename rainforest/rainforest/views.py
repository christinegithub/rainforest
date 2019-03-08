from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rainforest.models import Product
from rainforest.forms import ProductForm


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

def new_product(request):
    context = {'form': ProductForm()}
    response = render(request, 'new_product.html', context)
    return HttpResponse(response)

def product_created(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'new_product.html', {'form': ProductForm()})

def edit_product(request):
    context = {'form': ProductForm()}
    response = render(request, 'edit_product.html', context)
    return HttpResponse(response)

def product_edited(request):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'edit_product.html', {'form': ProductForm()})
