from django.urls import path
from .views import ReservationListCreateAPIView, ReservationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ReservationListCreateAPIView.as_view(), name='reservation-list-create'),
    path('<int:pk>/', ReservationRetrieveUpdateDestroyAPIView.as_view(), name='reservation-detail'),
]
