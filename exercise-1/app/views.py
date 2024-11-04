from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import *
# Create your views here.


def hey(request):
  form = HeyForm(request.GET)
  if form.is_valid():
    name = form.cleaned_data["name_data"]
    hey_name = f'Hey, {name}!'
    return render(request, "hey.html", {"form": form, "hey": hey_name })
  
  return render(request, "hey.html", {"form": form})

# -------------------------------------------------------------------------------------------------------------------------


def age_in(request):
  form = AgeForm(request.GET)
  if form.is_valid():
    end = form.cleaned_data["end"]
    birthyear = form.cleaned_data["birthyear"]
    age = end - birthyear
    print(age)
    return render(request, "age-in.html", {"form": form, "age": age})
  
  return render(request, "age-in.html", {"form": form})


def order(request):
  form = OrderForm(request.GET)
  if form.is_valid():

    burgers = form.cleaned_data["burgers"]
    fries = form.cleaned_data["fries"]
    drinks = form.cleaned_data["drinks"]

    total = (burgers * 4.50) + (fries * 1.50) + (drinks * 1.00)
    final = f'Your Total is ${total:.2f}!'
    return render(request, "order.html", {"form": form, "total" : final})

  return render(request, "order.html", {"form": form})