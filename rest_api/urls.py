from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('home/', home, name='home'),
    path('krosovka-api/', KrosovkaMakeAPI, name='KrosovkaMakeAPI'),
    path('Cars/', singlePAivewewe, name='singlePAivewewe'),
    path('krosovka-api/<int:pk>/', singleAPI),
    path('cars-api/<int:pk>/', singleApai),
]
