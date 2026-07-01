from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'user_type',
            'password'
        ]