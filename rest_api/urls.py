from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('home/', home, name='home'),
    path('krosovkaAPI/', KrosovkaMakeAPI, name='KrosovkaMakeAPI')
]
