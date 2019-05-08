from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_clients, name="list_clients"),
    path('actives/', views.list_clients_actives, name="list_clients_actives"),
    path('inactives/', views.list_clients_inactives, name="list_clients_inactives"),
    path('new/', views.new_client, name="new_client"),
    path('update/<int:id>/', views.update_client, name="update_client"),
    path('delete/<int:id>/', views.delete_client, name="delete_client"),
    path('show/<int:id>/', views.show_client, name="show_client"),
    path('change_status/<int:id>/', views.change_status, name="change_client_status"),
]
