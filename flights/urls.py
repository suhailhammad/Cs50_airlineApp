from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("<int:flight_id>", views.flight, name="flight"), # flight_id is a parameter accepted in flight page
  path("<int:flight_id>/book", views.book, name="book"), # flight_id is a parameter accepted in book page
]