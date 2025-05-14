from django.urls import path
from .views import FeedbackListCreateAPIView, FeedbackRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', FeedbackListCreateAPIView.as_view(), name='feedback-list-create'),
    path('<int:pk>/', FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='feedback-detail'),
]
