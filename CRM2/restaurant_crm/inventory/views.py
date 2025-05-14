from rest_framework import generics
from .models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class InventoryItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
