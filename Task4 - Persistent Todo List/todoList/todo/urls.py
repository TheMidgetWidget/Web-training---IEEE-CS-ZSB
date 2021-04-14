from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_item/<str:pk>/', views.updateItem, name="update_item"),
    path('delete_item/<str:pk>/', views.deleteItem, name="delete_item")
]