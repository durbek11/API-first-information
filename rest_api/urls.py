from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('home/', home, name='home'),
    path('krosovka-api/', KrosovkaMakeAPI, name='KrosovkaMakeAPI'),
    path('krosovka-api/<int:pk>/', singleAPI)
]
