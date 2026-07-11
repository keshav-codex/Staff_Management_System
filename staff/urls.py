from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 

    path('staff_list/', views.staff_list, name='staff_list'),

    path('add_staff/', views.add_staff, name='add_staff'),

    path("edit_staff/<int:id>/", views.edit_staff, name="edit_staff"),

    path("delete_staff/<int:id>/", views.delete_staff, name="delete_staff"),
]
