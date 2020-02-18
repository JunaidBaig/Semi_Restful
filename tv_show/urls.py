from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/', views.shows),
    path('shows/<int:show_id>', views.show_id),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/new', views.new_show_form),
    path('shows/new/process', views.add_show),
    path('shows/<int:show_id>/delete', views.delete_show)
]