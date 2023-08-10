from django.contrib import admin
from .models import CustomerContactInformation

@admin.register(CustomerContactInformation)
class CustomerContactInformationAdmin(admin.ModelAdmin):
    model=CustomerContactInformation
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


