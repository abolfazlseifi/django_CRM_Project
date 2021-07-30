from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from . import models,forms
# Create your views here.
from .models import Organization


class Organization_Form(CreateView):
    template_name = 'organization/form_organization.html'
    model = models.Organization
    form_class = forms.OrganizationForm
    queryset = Organization.objects.all()

class Organization_List(ListView):
    model = models.Organization
    template_name = "organization/list_organization.html"
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(expert_creator=self.request.user)
        return qs

class Organization_Detail(DetailView):
    template_name = 'organization/detail_organization.html'
    model = models.Organization
