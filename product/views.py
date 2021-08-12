from django.views.generic import ListView, CreateView
from organization.models import OrganizationProduct
from product.forms import ProductForm
from product.models import Product


# <--------------------| فرم ایجاد محصول |-------------------->

class CreatProductForm(CreateView):
    form_class = ProductForm
    template_name = 'products/product_form.html'
    model = Product
    success_url = 'homepage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization_products = OrganizationProduct.objects.all()
        context['organization_products'] = organization_products
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.save()
        return super().form_valid(form)


# <--------------------| لیست محصولات |-------------------->


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        search = self.request.GET.get('search', None)
        mode = self.request.GET.get('mode', None)
        if mode == 'name':
            products = Product.objects.filter(name__contains=search)
        elif mode == 'description':
            products = Product.objects.filter(description__contains=search)
        else:
            products = Product.objects.all()
        return products.order_by('pk')
