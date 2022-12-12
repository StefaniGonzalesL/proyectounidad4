from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",  "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class PortfolioProyectForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    image = forms.ImageField()
    url = forms.URLField()
    tags = forms.CharField(max_length=100)