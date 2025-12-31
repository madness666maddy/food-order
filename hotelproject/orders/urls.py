from django.urls import path
from .views import place_order, kitchen_dashboard, update_status

urlpatterns = [
    path('order/', place_order),
    path('kitchen/', kitchen_dashboard),
    path('kitchen/update/<int:order_id>/<str:status>/', update_status),
]
