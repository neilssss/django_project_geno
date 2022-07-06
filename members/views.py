#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from .models import Fish
from .models import Fish2
from .models import Cart
from .models import Wishlist
from .models import Order
from .models import OrderItem
from .models import Profile
from django.urls import reverse
from django.shortcuts import render,redirect
from .forms import Fish2Form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User



def registeruser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,("Registration Successful!"))
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request,'registeruser.html',{'form':form},)



def logoutuser(request):
    logout(request)
    messages.success(request,("You Were Log-out!!! "))
    return redirect('index')


def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request,("There was error loging in try again"))
            return redirect('loginuser')
            
    else:
        return render(request, 'loginuser.html',{})

def index(request):
    return render(request,'index.html',{})

def user(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('user.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    xx=x.upper()
    yy=y.upper()
    member = Members(first=xx,lastname=yy)
    member.save()
    return HttpResponseRedirect(reverse('user'))
def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('user'))
def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context ={
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
def updaterecord(request,id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.first = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('user'))

def display(request):
  my = Members.objects.all().values()
  template = loader.get_template('display.html')
  context = {
    'mymemberss': my,
  }
  return HttpResponse(template.render(context, request))

def home(request):
    return HttpResponseRedirect(reverse('index'))

def searchbar(request):
  searchbar = request.POST['searchbar']
  caps=searchbar.upper()
  my = Members.objects.all().values()
  #x=(searchbar:=my)
  template = loader.get_template('searchbar.html')
  context = {
    'mymember': my,
  }
  #return HttpResponse(template.render(context, request),{'searchbar':searchbar})
  return render(request,'searchbar.html',{'searchbar':caps,'mymember':my})

def buy(request):
    fish = Fish2.objects.all().values()
    template = loader.get_template('buy.html')
    context = {
        'fish' : fish,
    }
    return HttpResponse(template.render(context, request))

def addfish(request):
    template = loader.get_template('addfish.html')
    return HttpResponse(template.render({}, request))

def addfishrecord(request):
    x=request.POST['fish_type']
    y=request.POST['fish_name']
    w=request.POST['fish_size']
    xx=x.upper()
    yy=y.upper()
    ww=w.upper()
    member = Fish(fish_type=xx,fish_name=yy,fish_size=ww)
    member.save()
    return HttpResponseRedirect(reverse('buy'))
def deletefish(request, id):
    fish = Fish2.objects.get(id=id)
    fish.delete()
    return HttpResponseRedirect(reverse('buy'))
def updatefish(request, id):
    fish = Fish2.objects.get(id=id)
    template = loader.get_template('updatefish.html')
    context ={
        'fish': fish,
    }
    return HttpResponse(template.render(context, request))

def updatefishrecord(request,id):
    fish_type = request.POST['fish_type']
    fish_name = request.POST['fish_name']
    fish_size = request.POST['fish_size']
    fish = Fish2.objects.get(id=id)
    fish.fish_type = fish_type.upper()
    fish.fish_name = fish_name.upper()
    fish.fish_size = fish_size.upper()
    fish.save()
    return HttpResponseRedirect(reverse('buy'))


def addfish2(request):
    submitted = False
    if request.method == "POST":
        form = Fish2Form(request.POST,request.FILES)
        

        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/addfish2?submitted=True')
            return HttpResponseRedirect(reverse('buy'))
            #return HttpResponseRedirect('/addfish2')

    else:
        form = Fish2Form
        if 'submitted' in request.GET: 
            submitted = True      
    return render(request,'addfish2.html',{'form':form, 'submitted':submitted})

def buy1(request):
    fish = Fish2.objects.all()
    template = loader.get_template('buy1.html')
    context = {
        'fish' : fish,
    }
    return HttpResponse(template.render(context, request))

def searchbarfish(request):
    if request.method == "POST":
        searched = request.POST['searched']
        fish = Fish2.objects.filter(fish_type__contains=searched)
        return render(request,'searchbarfish.html',{'searched':searched,'fish':fish})
    else:
        return render(request,'searchbarfish.html',{})


def searchbarfishbuy(request):
    if request.method == "POST":
        searched = request.POST['searched']
        fish = Fish2.objects.filter(fish_type__contains=searched)
        return render(request,'searchbarfishbuy.html',{'searched':searched,'fish':fish})
    else:
        return render(request,'searchbarfishbuy.html',{})

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Fish2.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':"Product Already in Cart"})
                    
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.available_qty >= prod_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"Product added to Cart successfully"})
                       
                    else:
                        return JsonResponse({'status':"Only "+ str(product_check.available_qty)+" quantity available"})
            else:
                return JsonResponse({'status':"No such Product found"})
             
        else:
            return JsonResponse({'status':"Login to Continue"})  
           

    return redirect('addtocart')

def addtocart1(request, id):
    fish = Fish2.objects.get(id=id)
    template = loader.get_template('addtocart1.html')
    context ={
        'fish': fish,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='loginuser')
def cart(request):
    cart = Cart.objects.filter(user = request.user)
    context = {'cart':cart}
    return render(request,'cart.html',context)

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"Updated Successfully"})
    return redirect('cart')

def deletecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
        return JsonResponse({'status':"Deleted Cart Successfully"})
    return redirect('cart')

@login_required(login_url='loginuser')
def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'wishlist.html',context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Fish2.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse ({'status':"Product already in Wish List"})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':"Product added to Wish List"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login to Continue"})

    return redirect('cart')

def deletewishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlist = Wishlist.objects.get(product_id=prod_id)
                wishlist.delete()
                return JsonResponse ({'status':"Product remove in Wish List"})
            else:
                    
                return JsonResponse({'status':"Product not found in Wish List"})
        
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('wishlist')
@login_required(login_url='loginuser')
def checkout(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.available_qty :
            Cart.objects.all().delete(id=item.product_id)

    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.fish_price * item.product_qty

    userprofile = Profile.objects.filter(user=request.user).first()

    context = {'cartitems':cartitems,'total_price': total_price, 'userprofile':userprofile}
    return render(request,'checkout.html',context)

@login_required(login_url='loginuser')
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user.id):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.email = request.POST.get('email')
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.region = request.POST.get('region')
            userprofile.zipcode = request.POST.get('zipcode')
            userprofile.save()



        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.address = request.POST.get('address')
        neworder.phone = request.POST.get('phone')
        neworder.city = request.POST.get('city')
        neworder.region = request.POST.get('region')
        neworder.zipcode = request.POST.get('zipcode')

        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.fish_price * item.product_qty
        neworder.total_price = cart_total_price
        trackno = 'klay45'+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno)is None:
            track = 'klay45'+str(random.randint(1111111,9999999))
        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.fish_price,
                quantity=item.product_qty
                )
                #To decrease The product quantity from available stock
            orderproduct = Fish2.objects.filter(id=item.product_id).first()
            orderproduct.available_qty = orderproduct.available_qty - item.product_qty
            orderproduct.save()

                #clear user's cart
        Cart.objects.filter(user=request.user).delete()
        messages.success(request,"Your order has been placed successfully")
        payMode = request.POST.get('payment_mode')
        if(payMode == "Paid by Razor Pay"):
            return JsonResponse({'status':"Your order has been placed successfully"})

    return redirect('index')


def proceedtopay(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.fish_price * item.product_qty
    return JsonResponse({
        'total_price':total_price
        })
def myorder(request):
    orders = Order.objects.filter(user=request.user)
    context ={'orders':orders}
    return render(request,"myorder.html",context)
def myorderview(request,t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order, 'orderitems':orderitems}
    return render(request,"myorderview1.html",context)
