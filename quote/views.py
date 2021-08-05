# import weasyprint as weasyprint
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from quote.models import QuoteItem, Quote, QuoteFollowUp, QuoteEmailHistory, FollowUp
from quote.forms import QuoteForm
from django.contrib import messages
from organization.models import Organization
from . import tasks


class Quotes_Form(CreateView):
    template_name = 'quote/form_quote.html'
    model = QuoteItem
    form_class = QuoteForm

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizations'] = Organization.objects.all()
        return context


class ListQuotes(ListView):
    template_name = 'quote/list_quote.html'
    model = Quote
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_superuser:
            queryset = queryset.filter(creator=self.request.user)

        return queryset


class DetailQuotes(DetailView):
    template_name = 'quote/detail_quote.html'
    model = Quote

    def quotes_for_user_exists(self):
        qs = self.get_queryset()
        exists = qs.filter(creator=self.request.user).filter(pk=self.kwargs.get('pk', None)).exists()
        return exists

    def get(self, request, *args, **kwargs):
        if self.quotes_for_user_exists() or self.request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("quote:list_quote")


class DownloadQuote(DetailView):
    template_name = 'quote/pdf_quote.html'
    model = Quote

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        content = response.rendered_content
        # pdf = weasyprint.HTML(string=content, base_url='http://127.0.0.1:8000').write_pdf()
        # pdf_response = HttpResponse(content=pdf, content_type='application/pdf')
        # return pdf_response


def send_quote_email(request):
    tasks.send_email_task.delay()
    return HttpResponse("Done!")


class Follow_Up(ListView):
    template_name = 'quote/follow_up.html'
    model = FollowUp

    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.user.is_superuser:
            pk = self.kwargs.get('pk', None)
            qs = qs.filter(creator=self.request.user, pk=pk)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization_obj = get_object_or_404(klass='organization.Organization', pk=self.kwargs.get('pk', None))
        context['organization'] = organization_obj
        return context
