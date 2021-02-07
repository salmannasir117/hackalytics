from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name ='stocks'

urlpatterns = [
    path('', views.test_plot, name='index'),
    path('display_data', views.handle_checkboxes, name='display_data')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)