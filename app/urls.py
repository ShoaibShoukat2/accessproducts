from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index-page" ),
    
    path('details/<str:access_code>/',details, name='details-page'),
]



