from django.urls import path, include
from .views.busstopview import (
    BusStopListView,
    BusStopCreateView,
    BusStopDestroyView,
    BusStopUpdateView,
    BusStopRetrieveView,
    )
from .views.busview import (
    BusListView,
    BusCreateView,
    BusDestroyView,
    BusRetrieveView,
    BusUpdeteView,
)

from .views.authuser import (
    UserCreateView,
    UserListView,
    UserDestroyView,
    UserRetrieveView,
    UserUpdateView,
    LoginUser,
    LogoutUser,
)

app_name = 'bus_app'
urlpatterns = [

    path('user/login/',  LoginUser.as_view()),
    path('user/logout/', LogoutUser.as_view()),

    path('busstop/',          BusStopCreateView.as_view(), name='busstop'),
    path('busstop/list/',     BusStopListView.as_view(), name='busstop'),
    path('busstop/<int:pk>/', BusStopRetrieveView.as_view()),
    path('busstop/<int:pk>/', BusStopDestroyView.as_view()),
    path('busstop/<int:pk>/', BusStopUpdateView.as_view()),
    
    path('bus/list/',     BusListView.as_view()),
    path('bus/',          BusCreateView.as_view()),
    path('bus/<int:pk>/', BusUpdeteView.as_view()),
    path('bus/<int:pk>/', BusDestroyView.as_view()),
    path('bus/<int:pk>/', BusRetrieveView.as_view()),


    path('user/list/',     UserListView.as_view()),
    path('user/',          UserCreateView.as_view()),
    path('user/<int:pk>/', UserDestroyView.as_view()),
    path('user/<int:pk>/', UserUpdateView.as_view()),
    path('user/<int:pk>/', UserRetrieveView.as_view()),    
]
