from django.urls import path
from .views.busstopview import BusListCreateView, BusRetrieveUpdateDestroyView

urlpatterns = [
    path('buss/', BusListCreateView.as_view()),
    path('bus/<int:pk>/', BusRetrieveUpdateDestroyView.as_view()),
]
