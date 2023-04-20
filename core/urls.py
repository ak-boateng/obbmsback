from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('donor', views.donor, name='donor'),
    path('administrator', views.administrator, name='administrator'),
    path('adminsignup', views.adminsignup, name = 'adminsignup'), 
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('admins', views.admins, name='admins'),
    path('details/<str:dn>', views.details, name='details'),
]