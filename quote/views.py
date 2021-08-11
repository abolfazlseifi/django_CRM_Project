# import weasyprint as weasyprint
from django.core import mail
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView, CreateView
from quote.models import QuoteItem, Quote, FollowUp
from . import forms
from django.contrib import messages
from organization.models import Organization


class Quotes_Form(CreateView):
    template_name = 'quote/form_quote.html'

    def get_context_data(self, **kwargs):
        formset = forms.QuoteItemCreateFormSet(queryset=QuoteItem.objects.none())
        organizations = Organization.objects.filter(creator=self.request.user)
        return {'formset': formset, 'organizations': organizations}

    def post(self, *args, **kwargs):
        formset = forms.QuoteItemCreateFormSet(data=self.request.POST)
        if formset.is_valid():
            organization = get_object_or_404(Organization, pk=self.request.POST['organization'],
                                             creator=self.request.user)
            quote = Quote.objects.create(creator=self.request.user, organization=organization)
            for form in formset:
                form.instance.quote = quote
                form.save()
            messages.success(self.request, "ثبت شد")
            return redirect("quote:list_quote")


class ListQuotes(ListView):
    template_name = 'quote/list_quote.html'
    model = Quote
    paginate_by = 4


class DownloadQuote(DetailView):
    template_name = 'quote/pdf_quote.html'
    model = Quote

    # def get(self, request, *args, **kwargs):
        # response = super().get(request, *args, **kwargs)
        # content = response.rendered_content
        # pdf = weasyprint.HTML(string=content, base_url='http://127.0.0.1:8000').write_pdf()
        # pdf_response = HttpResponse(content=pdf, content_type='application/pdf')
        # return pdf_response

@require_http_methods(["GET"])
def send_quote_email(request,pk):
    quote = get_object_or_404(Quote, pk=pk, creator=request.user)
    text = render_to_string('quotetext.txt', {'object': quote})
    email = quote.organization.personnel_email
    sender = request.user.email
    emails = (
        ('Hello', text, sender, [email, ]),
    )
    results = mail.send_mass_mail(emails)
    print(results)
    messages.success(request, 'ایمیل با موفقیت ارسال شد.')
    return reverse_lazy('quote:list_quote')


class Follow_Up(CreateView):
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



class ListFollow_Up(ListView):
    template_name = 'quote/list_follow_up.html'
    model = FollowUp
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk', None)
        qs = qs.filter(organization__pk=pk)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        organization_obj = get_object_or_404(
            klass='organization.Organization',
            pk=self.kwargs.get('pk', None))

        context['organization'] = organization_obj

        return context