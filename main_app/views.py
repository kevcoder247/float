from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def home(request):
    return render(request,'home.html')


def about(request):
    return render(request, 'about.html')

'''
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
'''

def items_index(request):
   items = Item.objects.all()
   return render(request, 'items/index.html', {'items': items})


def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'items/detail.html', {'item' : item})

#Class Based Views
class ItemCreate(CreateView):
    model = Item
    fields = ['name', 'price', 'qty']


class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'price', 'qty']


class ItemDelete(DeleteView):
    model = Item
    success_url = '/items/'