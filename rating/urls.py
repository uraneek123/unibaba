from django.urls import path

from . import views

app_name = 'rating'

urlpatterns = [
    path('<int:pk>/', views.index, name='index'),
]
