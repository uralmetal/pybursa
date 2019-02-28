from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('<int:course_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('edit/<int:course_id>/', views.edit, name='edit'),
    path('remove/<int:course_id>/', views.remove, name='remove'),
]
