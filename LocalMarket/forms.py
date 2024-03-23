from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerUserForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email', 'username': 'Username', 'password1': 'Password', 'password2': 'Retype_Password'}

    def __init__(self, *args, **kwargs):
        super(CustomerUserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'cr-form-control'})

class ProfileForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'profile_image', 'address', 'city', 'zip_code']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})