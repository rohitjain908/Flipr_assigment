from django.urls import path
from . import views

urlpatterns = [
  path('',views.home),
  path('dashboard/<int:id>',views.dashboard,name="dashboard"),
  path('dashboard/resturant_details/<int:id>',views.resturant_details,name="resturant_details"),
  path('dashboard/add_dish/<int:owner_id>',views.add_dish,name="add_dish"),
  path('dashboard/edit_dish/<int:dish_id>',views.edit_dish,name="edit_dish"),
  path('dashboard/remove_dish/<int:dish_id>',views.remove_dish,name="remove_dish")

]