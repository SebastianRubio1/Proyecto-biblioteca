from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('biblioteca', views.index,name="Biblioteca"),
    path('libro', views.index,name="Libro")
]
