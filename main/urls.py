from django.urls import path
from .views import index, auth


urlpatterns = [
    path('', index),
    path('auth/', auth)
]