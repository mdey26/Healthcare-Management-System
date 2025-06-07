from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('search/', views.search_patient, name='search_patient'),
    path('list/', views.list_patients, name='list_patients'),
    path('update/<str:patient_id>/', views.update_patient, name='update_patient'),
    path('delete/<str:patient_id>/', views.delete_patient, name='delete_patient'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('analytics/conditions/', views.analytics_conditions, name='analytics_conditions'),
    path('', views.home_dashboard, name='home_dashboard'),
]
