from django.urls import path

from . import views

app_name = 'coaches'
urlpatterns = [
    path('<int:coach_id>/', views.detail, name='detail'),
]
