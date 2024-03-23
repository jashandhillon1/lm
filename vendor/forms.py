from django.forms import ModelForm
from .models import vendor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class VendorUserForm(UserCreationForm):
    class Meta:
        model = vendor
        fields = ['first_name', 'last_name', 'email', 'username', 'phone_number', 'password1', 'password2']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email', 'username': 'Username', 'phone_number': 'Phone Number', 'password1': 'Password', 'password2': 'Retype_Password'}

    def __init__(self, *args, **kwargs):
        super(VendorUserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'cr-form-control'})