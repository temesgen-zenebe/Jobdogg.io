from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from userContactInfo.models import CustomerContactInformation
from userContactInfo.forms import CustomerContactInformationForm

class CustomerContactInformationListView(ListView):
    model = CustomerContactInformation
    template_name = 'userContactInfo/customer_list.html'  # Provide the template path
    context_object_name = 'customers'

class CustomerContactInformationDetailView(DetailView):
    model = CustomerContactInformation
    template_name = 'userContactInfo/customer_detail.html'  # Provide the template path
    context_object_name = 'customer'

class CustomerContactInformationCreateView(CreateView):
    model = CustomerContactInformation
    form_class = CustomerContactInformationForm
    success_url = reverse_lazy('userContactInfo:customer-list')
    template_name = 'userContactInfo/customer_CreateView.html'  # Provide the template path

    def form_valid(self, form):
        # Additional logic if needed
        return super().form_valid(form)

class CustomerContactInformationUpdateView(UpdateView):
    model = CustomerContactInformation
    form_class = CustomerContactInformationForm
    template_name = 'userContactInfo/customer_updateView.html'  # Provide the template path

    def form_valid(self, form):
        # Additional logic if needed
        return super().form_valid(form)

class CustomerContactInformationDeleteView(DeleteView):
    model = CustomerContactInformation
    success_url = reverse_lazy('userContactInfo:customer-list')  # Provide the URL name for the list view
    template_name = 'userContactInfo/customer_confirm_delete.html'  # Provide the template path
