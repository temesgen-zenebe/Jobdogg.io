from django.urls import path

from userContactInfo.views import (
    CustomerContactInformationListView,
    CustomerContactInformationDetailView,
    CustomerContactInformationCreateView,
    CustomerContactInformationUpdateView,
    CustomerContactInformationDeleteView,
)

app_name = 'userContactInfo'

urlpatterns = [
    path('contactInformation/', CustomerContactInformationListView.as_view(), name='customer-list'),
    path('contactInformation/<slug:slug>/', CustomerContactInformationDetailView.as_view(), name='customer-detail'),
    path('contactInformation/create/', CustomerContactInformationCreateView.as_view(), name='customer-create'),
    path('contactInformation/<slug:slug>/update/', CustomerContactInformationUpdateView.as_view(), name='customer-update'),
    path('contactInformation/<slug:slug>/delete/', CustomerContactInformationDeleteView.as_view(), name='customer-delete'),
]
