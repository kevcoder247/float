from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.items_index, name='index'),
    path('items/<int:item_id>/', views.item_detail, name='detail'),
]