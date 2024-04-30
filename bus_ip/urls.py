from django.urls import path
from .views.busstopview import (
    BusStopListCreateView,
    BusStopRetrieveUpdateDestroyView,
    )
from .views.busview import (
    BusListCreateView,
    BusRetrieveUpdateDestroyView
)

urlpatterns = [
    path('busstops/', BusStopListCreateView.as_view()),
    path('busstop/<int:pk>/', BusStopRetrieveUpdateDestroyView.as_view()),
    
    path('buss/', BusListCreateView.as_view()),
    path('bus/<int:pk>/', BusRetrieveUpdateDestroyView.as_view()),
]
