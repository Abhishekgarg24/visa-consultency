from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='home'),
    path('contact',views.contact,name='home'),
    path('germany', views.germany, name='home'),
    path('australia', views.australia, name='home'),
    path('canada', views.canada, name='home'),
]