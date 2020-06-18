# coding: utf-8
from rest_framework import routers
from .views import filter_chain, filter_batch
from django.urls import path

router = routers.DefaultRouter()

urlpatterns = [
    path('filter_batch', filter_batch),
    path('filter_chain', filter_chain)
]
