from django.urls import path
from . import views

urlpatterns = [
    
    path('event/<str:pk>/', views.event_page, name='event'),

]