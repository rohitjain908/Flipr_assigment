from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Owner(models.Model):
  name=models.CharField(max_length=20)
  #we will use id field of owner for getting owner in views


class Dish(models.Model):
  owner=ForeignKey(Owner,on_delete=CASCADE,default=1)
  name=models.CharField(max_length=20)
  price=models.IntegerField()
  #image=models.ImageField()


class Resturant(models.Model):
  owner=ForeignKey(Owner,on_delete=CASCADE,default=1)
  name=models.CharField(max_length=20)
  address=models.CharField(max_length=200)
  latitude=models.IntegerField()
  longitude=models.IntegerField()
  opening_time=models.TimeField()
  closing_time=models.TimeField()
  bill_limit=models.IntegerField()
  #rating=models.FloatField()
  #menu:-list of all avalible dish
  #order_list:-
 




