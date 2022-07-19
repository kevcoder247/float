from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.items_index, name='index'),
    path('items/<int:item_id>/', views.item_detail, name='detail'),
    path('items/create/', views.ItemCreate.as_view(), name='item_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]