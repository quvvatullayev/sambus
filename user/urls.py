from django.urls import path
from views.userview import UserListCreateView, UserDetil

urlpatterns = [
    path('list/', UserListCreateView.as_view()),
    path('<int:pk>/', UserDetil.as_view()),
]