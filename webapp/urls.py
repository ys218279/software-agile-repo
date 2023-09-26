from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='' ),
    path('home',views.home, name='home' ),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    
    #CRUD - employees
    path('employee-records', views.employee_records, name='employee-records' ),
    path('view-employee-record/<int:pk>/', views.singular_employee_record, name="view-employee-record"),
    path('update-employee-record/<int:pk>/', views.update_employee_record, name="update-employee-record"),
    path('delete-record/<int:pk>', views.delete_record, name= "delete-record"),

    #CRUD - Tickets 
    path('create-ticket-record', views.create_ticket_record, name="create-ticketrecord"),
]