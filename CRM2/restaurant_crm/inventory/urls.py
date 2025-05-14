from django.urls import path
from .views import InventoryItemListCreateAPIView, InventoryItemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', InventoryItemListCreateAPIView.as_view(), name='inventory-list-create'),
    path('<int:pk>/', InventoryItemRetrieveUpdateDestroyAPIView.as_view(), name='inventory-detail'),
]
