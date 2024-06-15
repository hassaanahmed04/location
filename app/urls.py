from django.urls import path
from .views import *

urlpatterns = [
    # path('location/', get_location),
        path('get-location/', get_location, name='get_location'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('locations/',location_list, name='location_list'),
]   