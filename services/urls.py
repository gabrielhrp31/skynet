from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_services, name="list_services"),
    path('actives/', views.list_services_actives, name="list_services_actives"),
    path('inactives/', views.list_services_inactives, name="list_services_inactives"),
    path('show/<int:id>/', views.show_service, name="show_service"),
    path('new/', views.new_service, name="new_service"),
    path('update/<int:id>/', views.update_service, name="update_service"),
    path('delete/<int:id>/', views.delete_service, name="delete_service"),
    path('change_status/<int:id>/', views.change_status, name="change_service_status"),

    # urls da parte de contratos
    path('contracts/', views.list_contracts, name="list_contracts"),
    path('contracts/in_progress/', views.list_contracts_in_progress, name="list_contracts_in_progress"),
    path('contracts/finished/', views.list_contracts_finished, name="list_contracts_finished"),
    path('contracts/new/', views.new_contract, name="new_contract"),
    path('contracts/show/<int:id>', views.show_contract, name="show_contract"),
    path('contracts/edit/<int:id>/', views.update_contract, name="update_contract"),
    # path('contracts/new_to_service/<int:id>', views.new_contract, name="new_contract"),
    # path('contracts/new_to_client/<int:id>', views.new_contract, name="new_contract"),
    path('contracts/delete/<int:id>', views.delete_contract, name="delete_contract"),
]
