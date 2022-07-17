from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')


def about(request):
    return render(request, 'about.html')


#Seed Data
class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

items = [
    Item('Drill', '$8.99', 3),
    Item('TV', '$20.99', 7),
    Item('Car', '$99.99', 10),
    Item('Laptop', '$10.99', 3),
]

def items_index(request):
   #item = Item.objects.all()
    return render(request, 'items/index.html', {'items': items})
