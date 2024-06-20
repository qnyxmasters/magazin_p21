from django.urls import path

from apps.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list')
]