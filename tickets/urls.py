from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index),
    path('<int:confirmation_number>', views.ticket_search),
]