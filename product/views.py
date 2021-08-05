from django.views.generic import ListView, CreateView
from organization.models import OrganizationProduct
from product.forms import ProductForm
from product.models import Product


class CreatProductForm(CreateView):
    form_class = ProductForm
    template_name = 'products/product_form.html'
    model = Product
    success_url ='homepage'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization_products = OrganizationProduct.objects.all()
        context['organization_products'] = organization_products
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.save()
        return super().form_valid(form)


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6


