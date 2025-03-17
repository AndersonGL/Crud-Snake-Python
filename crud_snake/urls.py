
from django.contrib import admin
from django.urls import path
from meuapp.views import home, form, create, view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),  # Criando a rota create
    path('view/<int:pk/', view, name='view'),
]


