from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('home/', home, name='home'),
    path('krosovka-api/', KrosovkaMakeAPI, name='KrosovkaMakeAPI'),
    path('Cars/', singlePAivewewe, name='singlePAivewewe'),
    path('fruit/', FruitsAPI, name='FruitsAPI'),
    path('krosovka-api/<int:pk>/', singleAPI),
    path('cars-api/<int:pk>/', singleApai),
    path('create/', malumotJoylash),
    path('update/<int:pk>/', malumotUpdate),
    path('delete/<int:pk>/', malumotDelete)
]
