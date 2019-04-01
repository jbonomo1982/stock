from django.urls import path
from . import views


urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('prov/', views.prov, name='prov'),
]
