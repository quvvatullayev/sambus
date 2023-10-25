from django.urls import path
from .views.buss import BussDetilView, BussListCreateView
from .views.bus import BusListCreateView, BusDetilView

urlpatterns = [
    # Buss views
    path('buss/list/', BussListCreateView.as_view()),
    path('buss/<int:pk>/', BussDetilView.as_view()),

    # Bus views
    path('bus/lsit/', BusListCreateView.as_view()),
    path('bus/<int:pk>/', BusDetilView.as_view())
]