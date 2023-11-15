from django.urls import path
from views.userview import UserListCreateView, UserDetil, UserFindNearestStation

urlpatterns = [
    path('list/', UserListCreateView.as_view()),
    path('<int:pk>/', UserDetil.as_view()),

    path('station/<int:pk>/', UserFindNearestStation.as_view())
]