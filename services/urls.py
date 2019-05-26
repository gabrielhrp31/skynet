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
    path('contracts/in_progress/', views.list_contracts, name="list_contracts_in_progress"),
    path('contracts/finished/', views.list_contracts, name="list_contracts_finished"),
    path('contracts/new/', views.list_contracts, name="new_contract"),
]
