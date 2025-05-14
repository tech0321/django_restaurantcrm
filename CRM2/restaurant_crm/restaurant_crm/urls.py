from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/dashboard.html'), name='home'),
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/customers/', include('customers.urls')),
    path('api/reservations/', include('reservations.urls')),
    path('api/employees/', include('employees.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/feedback/', include('feedback.urls')),

    # Frontend pages using TemplateView
    path('dashboard/', TemplateView.as_view(template_name='dashboard/dashboard.html'), name='dashboard'),
    path('customers/', TemplateView.as_view(template_name='customers/customers.html'), name='customers'),
    path('reservations/', TemplateView.as_view(template_name='reservations/reservations.html'), name='reservations'),
    path('employees/', TemplateView.as_view(template_name='employees/employees.html'), name='employees'),
    path('orders/', TemplateView.as_view(template_name='orders/orders.html'), name='orders'),
    path('inventory/', TemplateView.as_view(template_name='inventory/inventory.html'), name='inventory'),
    path('feedback/', TemplateView.as_view(template_name='feedback/feedback.html'), name='feedback'),
]
