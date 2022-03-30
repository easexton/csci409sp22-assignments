from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index),
    path('/<str:airport_code>', views.airport_info),
]