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
    Login_user,
    Logout_user,
)

app_name = 'bus_app'
urlpatterns = [
    path('busstop', BusStopListCreateView.as_view(), name='busstop'),
    path('busstop/<int:pk>/', BusStopRetrieveUpdateDestroyView.as_view()),
    
    path('bus', BusListCreateView.as_view()),
    path('bus/<int:pk>/', BusRetrieveUpdateDestroyView.as_view()),

    path('user', UserListCreateView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),

    path('user/login/', Login_user.as_view()),
    path('user/logout/', Logout_user.as_view()),
]
