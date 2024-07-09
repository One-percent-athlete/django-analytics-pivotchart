from django.urls import path
from . import views

urlpatterns = [
    path('', views.pivot_dash, name='pivot_dash'),
    path('data', views.pivot_data, name='pivot_data'),
]