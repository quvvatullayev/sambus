from django.urls import path, include
from .views.busstopview import (
    BusStopListCreateView,
    BusStopRetrieveUpdateDestroyView,
    )
from .views.busview import (
    BusListCreateView,
    BusRetrieveUpdateDestroyView,
)

from .views.authuser import (
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
)

app_name = 'bus_app'
urlpatterns = [
    path('busstops/', BusStopListCreateView.as_view(), name='busstop'),
    path('busstop/<int:pk>/', BusStopRetrieveUpdateDestroyView.as_view()),
    
    path('buss/', BusListCreateView.as_view()),
    path('bus/<int:pk>/', BusRetrieveUpdateDestroyView.as_view()),

    path('users/', UserListCreateView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
]
