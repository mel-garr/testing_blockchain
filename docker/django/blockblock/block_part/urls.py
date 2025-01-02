from django.urls import path
from .views import *

urlpatterns =[
    path('', home_view),
    path('send_letter/', send_to_back, name='send_letter'),
    # path('send_to_back/', send_to_back),
]