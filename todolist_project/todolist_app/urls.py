from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<uuid:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<uuid:item_id>/', views.delete_item, name='delete_item'),
]
