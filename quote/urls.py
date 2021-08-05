from django.urls import path
from .views import Quotes_Form, ListQuotes, DetailQuotes, DownloadQuote, send_quote_email, Follow_Up

app_name = 'quote'
urlpatterns = [
    path('formquote', Quotes_Form.as_view(), name='form_quote'),
    path('listquote', ListQuotes.as_view(), name='list_quote'),
    path('detailquote/<int:pk>/', DetailQuotes.as_view(), name='detail_quote'),
    path('download/<int:pk>/', DownloadQuote.as_view(), name='pdf_quote'),
    path('email/', send_quote_email, name='email_quote'),
    path('followup/<int:pk>/', Follow_Up.as_view(), name='follow_up'),

]
