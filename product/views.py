from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from product.forms import ProductForm
from product.models import Product
from product_category.models import ProductCategory


class CreatProductForm(CreateView):
    form_class = ProductForm
    template_name = 'products/product_form.html'
    model = Product
    success_url ='homepage'





class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        print(self.kwargs)
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)


def product_detail(request, *args, **kwargs):
    product_id = kwargs['productId']

    product = Product.objects.get_by_id(product_id)

    # print(product.tag_set.all())

    if product is None or not product.tax:
        raise Http404('محصول مورد نظر یافت نشد')

    context = {
        'product': product
    }

    # tag = Tag.objects.first()
    # print(tag.products.all())
    # print(product.tag_set.all())

    return render(request, 'products/product_detail.html', context)


class SearchProductsView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()


def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/products_categories_partial.html', context)
