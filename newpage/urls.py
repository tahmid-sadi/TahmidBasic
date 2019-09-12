from django.urls import path
from . import views


urlpatterns = [
    path('', views.newfront, name='newfront'),
    path('frontdetail', views.frontdetail, name='frontdetail'),
]