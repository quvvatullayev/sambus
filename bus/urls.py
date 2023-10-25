from django.urls import path
from .views.buss import BussDetilView, BussListCreateView

urlpatterns = [
    path('buss/list/', BussListCreateView.as_view()),
    path('buss/<int:pk>/', BussDetilView.as_view()),
]