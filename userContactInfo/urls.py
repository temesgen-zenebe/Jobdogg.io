from django.urls import path

from userContactInfo.views import (
    CustomerContactInformationListView,
    CustomerContactInformationDetailView,
    CustomerContactInformationCreateView,
    CustomerContactInformationUpdateView,
    CustomerContactInformationDeleteView,
    SuccessConfirmationView,
)

app_name = 'userContactInfo'

urlpatterns = [
    path('', CustomerContactInformationCreateView.as_view(), name='customer-create'),
    path('successConfirmation/', SuccessConfirmationView.as_view(), name='success-Confirmation'),
    path('contactInformation/', CustomerContactInformationListView.as_view(), name='customer-list'),
    path('contactInformation/<slug:slug>/', CustomerContactInformationDetailView.as_view(), name='customer-detail'),
    path('contactInformation/<slug:slug>/update/', CustomerContactInformationUpdateView.as_view(), name='customer-update'),
    path('contactInformation/<slug:slug>/delete/', CustomerContactInformationDeleteView.as_view(), name='customer-delete'),
    
]
