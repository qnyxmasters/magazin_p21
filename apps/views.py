from django.views.generic import ListView

from apps.models import Product, Category


class ProductListView(ListView):
    queryset = Product.objects.order_by('-created_at')
    template_name = 'apps/product/product-list.html'
    context_object_name = 'products'
