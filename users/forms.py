from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
import django.forms as forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2",]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password",]
