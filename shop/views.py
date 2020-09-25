from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Product.objects.all()

    ''' 
    creating search funtionality always work into forms
    '''

    search1 = request.GET.get("search1")
    if search1 != "" and search1 is not None:
        product_objects = product_objects.filter(title__icontains=search1)


    #pagination code

    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'shop/index.html',{"product_objects":product_objects})


def productview(request,id):

    product_object = Product.objects.get(id=id)
    
    return render(request,'shop/productview.html',{"product_object":product_object})


def about(request):
    
    return render(request,'shop/about.html')


def contact(request):
    
    return render(request,'shop/contact.html')

def tracker(request):
    
    return render(request,'shop/tracker.html')



def checkout(request):
    
    return render(request,'shop/checkout.html')