

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicle/', views.vehicle_list, name='vehicle_list'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/create/', views.vehicle_create, name='vehicle_create'),
    path('vehicle/<int:pk>/edit/', views.vehicle_edit, name='vehicle_edit'),
    path('vehicle/<int:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]