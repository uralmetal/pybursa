from django.urls import path

from . import views

app_name = 'students'
urlpatterns = [
    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail'),
    path('', views.StudentListView.as_view(), name='list'),
    path('add/', views.StudentCreateView.as_view(), name='create'),
    path('remove/<int:pk>/', views.StudentDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', views.StudentUploadView.as_view(), name='edit'),
]
