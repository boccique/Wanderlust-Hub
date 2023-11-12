from django.forms import ModelForm
from .models import RegisteredUser


class RegisteredUserForm(ModelForm):
    class Meta:
        model = RegisteredUser
        fields = ('email', 'passwd')
