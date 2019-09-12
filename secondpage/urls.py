from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.secondfront, name='secondfront'),
    path('seconddetail', views.seconddetail, name='seconddetail'),
]