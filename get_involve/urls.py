from django.urls import path
from . import views



urlpatterns = [
    path('', views.get_involve, name='get_involve'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('volunteer_form/', views.volunteer_form, name='volunteer_form'),
    path('join_us/', views.join_us, name='join_us'),
    path('join_us_form/', views.join_us_form, name='join_us_form'),
    ]


