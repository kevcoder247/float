from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'item_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for item_id: {self.item_id} @{self.url}" 