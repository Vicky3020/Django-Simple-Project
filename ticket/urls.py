from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tic_detail/<int:id>/', views.tic_detail, name='tic-detail'),
    path('add_place/', views.add_place, name='add-place'),
    path('edit_bus/<int:id>/', views.edit_bus, name='edit-bus'),
    path('delete_bus/<int:id>/', views.delete_bus, name='delete-bus'),
]