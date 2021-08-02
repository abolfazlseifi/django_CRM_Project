from django.urls import path
from .views import ProductsList, product_detail, SearchProductsView, \
    ProductsListByCategory, products_categories_partial,CreatProductForm

app_name = 'product'

urlpatterns = [
    path('productform', CreatProductForm.as_view(),name='product_form'),
    path('products', ProductsList.as_view()),
    path('products/<category_name>', ProductsListByCategory.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
    path('products_categories_partial', products_categories_partial, name='products_categories_partial'),
    ]