from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index),
    path('search/<str:origin>/<str:destination>', views.route_search),
]