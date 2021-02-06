from django.urls import path

from . import views

app_name ='stocks'

urlpatterns = [
    path('', views.test_plot, name='index'),
    path('bootstrap/', views.test_bootstrap, name='bootstrap'),
    
] 