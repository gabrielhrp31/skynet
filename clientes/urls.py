from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_clients, name="list_clients"),
    path('new/', views.new_client, name="new_client"),
    path('update/<int:id>/', views.update_client, name="update_client"),
    path('delete/<int:id>/', views.delete_client, name="delete_client")
]
