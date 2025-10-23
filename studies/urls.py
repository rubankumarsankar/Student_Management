from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('add/', views.study_create, name='study_create'),
    path('view/<int:pk>/', views.study_view, name='study_view'),
    path('edit/<int:pk>/', views.study_update, name='study_update'),
    path('delete/<int:pk>/', views.study_delete, name='study_delete'),
]
