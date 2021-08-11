from django.urls import path
from .views import Quotes_Form, ListQuotes, DownloadQuote, send_quote_email, Follow_Up, ListFollow_Up

app_name = 'quote'
urlpatterns = [
    path('formquote', Quotes_Form.as_view(), name='form_quote'),
    path('listquote', ListQuotes.as_view(), name='list_quote'),
    path('download/<int:pk>/', DownloadQuote.as_view(), name='pdf_quote'),
    path('email/<int:pk>', send_quote_email, name='email_quote'),
    path('followup/<int:pk>/', Follow_Up.as_view(), name='follow_up'),
    path('listfollowup/<int:pk>/', ListFollow_Up.as_view(), name='list_follow_up'),

]
