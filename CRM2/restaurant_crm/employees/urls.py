from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),
]
