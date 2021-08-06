from django.urls import path
from .views import ProductsList,CreatProductForm

app_name = 'product'

urlpatterns = [
    path('productform', CreatProductForm.as_view(),name='product_form'),
    path('products', ProductsList.as_view(),name='product_list'),

    ]