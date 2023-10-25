from django.urls import path
from .views.buss import BussDetilView, BussListCreateView
from .views.bus import BusListCreateView, BusDetilView
from .views.route import RouteListCreateView, RouteDetilView
from .views.station import StationListCreateView, StationDetilView

urlpatterns = [
    # Buss views
    path('buss/list/', BussListCreateView.as_view()),
    path('buss/<int:pk>/', BussDetilView.as_view()),

    # Bus views
    path('bus/lsit/', BusListCreateView.as_view()),
    path('bus/<int:pk>/', BusDetilView.as_view()),

    # Route views
    path('route/lsit/', RouteListCreateView.as_view()),
    path('route/<int:pk>/', RouteDetilView.as_view()),

    # Station views
    path('station/list/', StationListCreateView.as_view()),
    path('station/<int:pk>/', StationDetilView.as_view()),
]