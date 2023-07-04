from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Product
from .forms import ProductForm
from django.urls import reverse


def create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    
    context = {'form': form, 'back_url': reverse('list_view')}
    return render(request, 'create_view.html', context)



def list_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'list_view.html', context)

def detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    context = {'product': product, 'back_url': reverse('list_view')}
    return render(request, 'detail_view.html', context)

def update_view(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    
    context = {'form': form, 'product': product, 'back_url': reverse('list_view')}
    return render(request, 'update_view.html', context)

def delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return HttpResponseRedirect('/')
    
    context = {'product': product, 'back_url': reverse('list_view')}
    return render(request, 'delete_view.html', context)