from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'phone',
            'telegram',
            'country',
            'photo',
        )
        labels = {
            'username': 'Username',
            'password': 'Password',
            'first_name':'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'phone': 'Mobile phone',
            'telegram': 'Telegram account',
            'country': 'Where are you from?',
            'photo': 'Photo',
        }
