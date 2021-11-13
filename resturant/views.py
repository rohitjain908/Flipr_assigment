from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Owner,Resturant,Dish


# Create your views here.

def home(request):
  # owner_list=Owner.objects.all()
  # #print(owner_list[0].name)
  # return render(request,'resturant/home.html',{
  #   'owners_list':owner_list
  # })
  if request.method=="POST":
    username=request.POST["username"]
    if Owner.objects.all().filter(name=username).exists():
      owner=Owner.objects.get(name=username)
      print(owner.id)
      return redirect("dashboard",id=owner.id) 


  return render(request,'resturant/home.html')


def dashboard(request,id):
  owner=Owner.objects.get(id=id)
  resturant=None
  dishes=None
  if Resturant.objects.all().filter(owner=owner):
    resturant=Resturant.objects.get(owner=owner)

  if Dish.objects.all().filter(owner=owner):
    dishes=Dish.objects.all().filter(owner=owner)
  
  return render(request,'resturant/dashboard.html',{
    'name':owner.name,
    'id':id,
    'resturant':resturant,
    'dishes':dishes
    })





def resturant_details(request,id):
  owner=Owner.objects.get(id=id)
  if request.method=="POST":
    name=request.POST["name"]
    address=request.POST["address"]
    latitude=request.POST["latitude"]
    longitude=request.POST["longitude"]
    opening_time=request.POST["opening_time"]
    closing_time=request.POST["closing_time"]
    bill_limit=request.POST["bill_limit"]

    if Resturant.objects.all().filter(owner=owner).exists():
      Resturant.objects.all().filter(owner=owner).update(
        owner=owner,
        name=name,
        address=address,
        latitude=latitude,
        longitude=longitude,
        opening_time=opening_time,
        closing_time=closing_time,
        bill_limit=bill_limit
      )
    else:
      Resturant.objects.create(
        owner=owner,
        name=name,
        address=address,
        latitude=latitude,
        longitude=longitude,
        opening_time=opening_time,
        closing_time=closing_time,
        bill_limit=bill_limit
      )

    return redirect("dashboard",id=id)

  return render(request,'resturant/resturant_details.html')

def add_dish(request,owner_id):
  owner=Owner.objects.get(id=owner_id)

  if request.method=="POST":
    name=request.POST["name"]
    price=request.POST["price"]

    Dish.objects.create(
      owner=owner,
      name=name,
      price=price
    )


  return render(request,'resturant/add_dish.html')

def edit_dish(request,dish_id):
  if request.method=="POST":
    name=request.POST["name"]
    price=request.POST["price"]

    Dish.objects.all().filter(id=dish_id).update(
      name=name,
      price=price
    )


  dish=Dish.objects.get(id=dish_id)
  return render(request,'resturant/edit_dish.html',{
    'dish':dish
  })

def remove_dish(request,dish_id):
  instance=Dish.objects.get(id=dish_id)
  instance.delete()

  return HttpResponse("removed")

