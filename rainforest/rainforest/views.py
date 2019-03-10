from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rainforest.models import Product, Review
from rainforest.forms import ProductForm, ReviewForm


def root(request):
    return HttpResponseRedirect('/home')

def home_page(request):
    context = {'products': Product.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def product_show(request, id):
    product = Product.objects.get(pk=id)
    context = {'product': product, 'form': ReviewForm()}
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

def edit_product(request,id):
    product = Product.objects.get(pk=id)
    context = {'form': ProductForm(instance=product), 'product': product}
    response = render(request, 'edit_product.html', context)
    return HttpResponse(response)

def product_edited(request,id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'edit_product.html', {'form': ProductForm(instance=product), 'product': product})

def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect('/home')

def new_review(request,product_id):
    product = Product.objects.get(pk=product_id)
    # request.POST['product']
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.instance
        review.product = product
        review.save()
        return HttpResponseRedirect(reverse('product_details', args=[product.pk]))
    else:
        return render(request, 'product.html', {'form': ReviewForm()})

def edit_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    context = {'form': ReviewForm(instance=review), 'review': review}
    response = render(request, 'edit_review.html', context)
    return HttpResponse(response)

def review_edited(request, review_id):
    review = Review.objects.get(pk=review_id)
    form = ReviewForm(request.POST, instance=review)
    if form.is_valid():
        edited_review = form.save()
        return HttpResponseRedirect(reverse('product_details', args=[review.product.pk]))
    else:
        return render(request, 'edit_review.html', {'form': ReviewForm(instance=review), 'review': review})
