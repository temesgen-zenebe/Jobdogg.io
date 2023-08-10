from django import forms
from userContactInfo.models import CustomerContactInformation

class CustomerContactInformationForm(forms.ModelForm):
    class Meta:
        model = CustomerContactInformation
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
        
        help_texts = {
            'email': 'Please enter your valid email ex. exapmle@email.com.',
            'phone_number': 'Please enter your valid phone number.',
            'address': 'Please enter your valid state, zipcode.',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'emailinput form-control form-control-sm'}),
            'address': forms.TextInput(attrs={'class': 'textinput form-control form-control-sm', 'placeholder': '1234 Main St'}),
            'phone_number': forms.TextInput(attrs={'class': 'textinput form-control form-control-sm'}),
         }