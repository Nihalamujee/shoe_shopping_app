from django.http import JsonResponse
from django.shortcuts import redirect, render
from Shop.form import CustomUserForm,BrandForm,ProductForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
from django.http import HttpResponseRedirect
from django.views import View

def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,"Shop/index.html",{"products":products})

def userhome(request):
    products=Product.objects.filter(trending=1)
    return render(request,"Shop/userindex.html",{"products":products})


def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success ,You can Login now..")
            return redirect('/login')
        else:
            messages.error(request,"form is not valid")
    else:
        return render(request,"Shop/register.html",{'form':form})





def login_page(request):
    if request.user.is_authenticated:
        return redirect("/userhome")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            eml=request.POST.get('email')
            user=authenticate(request,username=name,password=pwd,email=eml)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/userhome")
            else:
                messages.error(request,"Invalid User Name or Password or email")
                return redirect('/login')
        else:
            return render(request,"Shop/login.html")



def collections(request):
    brand=Brand.objects.filter(status=0)
    return render(request,"Shop/collections.html",{"brand":brand})


def collectionsview(request,name):
    if(Brand.objects.filter(name=name,status=0)):
        products=Product.objects.filter(brand__name=name)
        return render(request, "Shop/products/index.html",{"products":products,"brand_name":name})
    else:
        messages.warning(request,"No such Brand Found")
        return redirect('/collections')



def product_details(request,bname,pname):
    if(Brand.objects.filter(name=bname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"no such Product Found")
            return redirect('/collections')
    else:
        messages.error(request,"No such Brand Found")
        return redirect('/collections')





def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"Shop/cart.html",{"cart":cart})
    else:
        return redirect("/login")





def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
       if request.user.is_authenticated:
        data=json.load(request)
        product_qty=data['product_qty']
        product_id=data['pid']
        product_status=Product.objects.get(id=product_id)
        if product_status:
            if Cart.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status':'Product Already in Cart'},status=200)
            else:
                if product_status.quantity>=product_qty:
                    Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                    return JsonResponse({'status':'Product Added to Cart'},status=200)
                else:
                    return JsonResponse({'status':'Product Stock Not Available'},status=200)

       else:
         return JsonResponse({'status':'Login to Add a product in Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)




def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

class checkout(View):
    def get(self,request):
        return render(request,'Shop/checkout.html',locals())




def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
       if request.user.is_authenticated:
        data=json.load(request)
        product_id=data['pid']
        product_status=Product.objects.get(id=product_id)
        if product_status:
            if Favourite.objects.filter(user=request.user,product_id=product_id):
                return JsonResponse({'status':'Product Already in Favourite'},status=200)
            else:
                Favourite.objects.create(user=request.user, product_id=product_id)
                return JsonResponse({'status': 'Product Added to Favourite'},status=200)

       else:
         return JsonResponse({'status':'Login to Add a product in Favourite'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)






def favviewpage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,"Shop/fav.html",{"fav":fav})
    else:
        return redirect("/login")




def remove_fav(request,fid):
    item=Favourite.objects.get(id=fid)
    item.delete()
    return redirect("/favviewpage")







def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
    return redirect("/home")


def admin_page(request):

    return render(request,"front/index.html")


def my_login(request):
    if request.user.is_authenticated:
        return redirect("/admin_page")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')

            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/admin_page")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect('/my_login')
        else:
            return render(request,'front/login.html')


def admin_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
    return redirect("/home")


def all_brands(request):
    brands_list=Brand.objects.all()
    return render(request,'front/edit_brands.html',{'brands_list':brands_list})

def add_brands(request):
    submitted=False
    if request.method=="POST":
        form=BrandForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_brands?submitted=True')
    else:
        form=BrandForm
        if 'submitted' in request.GET:
            submitted=True

        return render(request,'front/add_brands.html',{'form':form,'submitted':submitted})



def all_products(request):
    products_list=Product.objects.all()
    return render(request,'front/edit_products.html',{'products_list':products_list})



def add_products(request):
    submitted = False
    if request.method == "POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_products?submitted=True')
    else:
        form=ProductForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'front/add_products.html',{'form':form,'submitted':submitted})

def delete_brands(request,bid):
    brands=Brand.objects.get(id=bid)
    brands.delete()
    return redirect('/brands')


def delete_products(request,pid):
    products=Product.objects.get(id=pid)
    products.delete()
    return redirect('/products')

