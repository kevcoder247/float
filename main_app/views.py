from django.shortcuts import render, redirect
from .models import Item, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/' 

BUCKET = 'float-app-bucket'


# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request,'home.html', {'items': items})

def about(request):
    print(request.user)
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

@login_required
def items_index(request):
   items = Item.objects.filter(user=request.user)
   return render(request, 'items/index.html', {'items': items})

@login_required
def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    user = request.user
    return render(request, 'items/detail.html', {'item' : item, 'current_user': user})



def add_photo(request, item_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, item_id=item_id)
            photo.save()
        except:
            print('An error occured uploading photo')
            return redirect('detail', item_id=item_id)

        return redirect('detail', item_id=item_id)



#Class Based Views
class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'price', 'qty']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'price', 'qty']


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/items/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context) 










