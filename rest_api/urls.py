from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('', home, name='home'),
    path('krosovka-api/', KrosovkaMakeAPI, name='KrosovkaMakeAPI'),
    path('Cars/', singlePAivewewe, name='singlePAivewewe'),
    path('krosovka-api/<int:pk>/', singleAPI),
    path('cars-api/<int:pk>/', singleApai),
    path('create/', malumotJoylash),
    path('update/<int:pk>/', malumotUpdate),
    path('delete/<int:pk>/', malumotDelete),
    path('search/', krosovkaSearch, name="search"),
    path('filter-bazm/', filterKrosovka, name='filter-bazm'),
    path('filter-sport/', filterKrosovkabro, name='filter-sport')
]
