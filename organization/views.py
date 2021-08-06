from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . import models, forms


class Organization_Form(CreateView):
    model = models.Organization
    form_class = forms.OrganizationForm
    template_name = 'organization/form_organization.html'
    success_url = reverse_lazy('organization:list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return super().form_invalid(form)


class Organization_List(ListView):
    model = models.Organization
    template_name = "organization/list_organization.html"
    paginate_by = 6

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     if not self.request.user.is_superuser:
    #         qs = qs.filter(creator=self.request.user)
    #     return qs


class Organization_Detail(DetailView):
    model = models.Organization
    template_name = 'organization/detail_organization.html'

    def get_queryset(self):
        organization = models.Organization.objects.filter(pk=self.kwargs['pk'], creator=self.request.user)
        return organization



class Organization_update(UpdateView):
    model = models.Organization
    template_name = 'organization/update_organization.html'
    form_class = forms.OrganizationForm

    def get_queryset(self):
        organization = models.Organization.objects.filter(pk=self.kwargs['pk'], creator=self.request.user)
        return organization

    def get_success_url(self):
        return redirect ('organization:detail', kwargs={'pk': self.object.pk})