from django.urls import path
from .views import CreateBusStop

urlpatterns = [
    path('create_busstop/', CreateBusStop.as_view())
]
