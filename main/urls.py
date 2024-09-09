from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Link to the home page
]
