from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from .models import Contact
from math import ceil

# Create your views here.

def index(request):
    product_objects = Product.objects.all()

    ''' 
    creating search funtionality always work into forms
    '''

    search1 = request.GET.get("search1")
    if search1 != "" and search1 is not None:
        product_objects = product_objects.filter(title__icontains=search1)


    #pagination code for number od slides

    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'shop/index.html',{"product_objects":product_objects})
   



def productview(request,id):

    product_object = Product.objects.get(id=id)
    
    return render(request,'shop/productview.html',{"product_object":product_object})


# // to get the items in checkout form
def checkout(request):

    if request.method=="POST":
        
        items =request.POST['items']
        name =request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        total=request.POST['total']

        ins=Contact( items=items, name=name , email=email, phone=phone, address=address,total=total)
        ins.save()

    return render(request,'shop/checkout.html')





    