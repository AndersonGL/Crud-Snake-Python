from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_word,
    name='hello_word'),
]

