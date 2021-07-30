from django.urls import path
from .views import Organization_Form,Organization_List,Organization_Detail

urlpatterns = [
    path('form',Organization_Form.as_view()),
    path('list',Organization_List.as_view()),
    path('detail/<pk>',Organization_Detail.as_view()),
    ]
