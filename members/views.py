#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from .models import Fish
from django.urls import reverse
from django.shortcuts import render
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
    fish = Fish.objects.all().values()
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
    z=request.POST['fish_price']
    xx=x.upper()
    yy=y.upper()
    ww=w.upper()
    zz=z.upper()
    member = Fish(fish_type=xx,fish_name=yy,fish_size=ww,fish_price=zz)
    member.save()
    return HttpResponseRedirect(reverse('buy'))
def deletefish(request, id):
    fish = Fish.objects.get(id=id)
    fish.delete()
    return HttpResponseRedirect(reverse('buy'))
def updatefish(request, id):
    fish = Fish.objects.get(id=id)
    template = loader.get_template('updatefish.html')
    context ={
        'fish': fish,
    }
    return HttpResponse(template.render(context, request))
def updatefishrecord(request,id):
    fish_type = request.POST['fish_type']
    fish_name = request.POST['fish_name']
    fish_size = request.POST['fish_size']
    fish_price = request.POST['fish_price']
    fish = Fish.objects.get(id=id)
    fish.fish_type = fish_type.upper()
    fish.fish_name = fish_name.upper()
    fish.fish_size = fish_size.upper()
    fish.fish_price = fish_price.upper()
    fish.save()
    return HttpResponseRedirect(reverse('buy'))


       