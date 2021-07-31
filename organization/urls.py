from django.urls import path
from .views import Organization_Form, Organization_List

app_name = 'organization'
urlpatterns = [
    path('form', Organization_Form.as_view(), name='form'),
    path('list', Organization_List.as_view(), name="list"),
    # path('detail', Organization_Detail.as_view(), name="detail"),
]
