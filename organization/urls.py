from django.urls import path
from .views import Organization_Form,Organization_List,Organization_Detail, Organization_update

app_name = 'organization'
urlpatterns = [
    path('formorg',Organization_Form.as_view(),name='form'),
    path('listorg',Organization_List.as_view(),name='list'),
    path('detailorg/<int:pk>',Organization_Detail.as_view(),name='detail'),
    path('updateorg/<int:pk>',Organization_update.as_view(),name="Update"),
    ]
