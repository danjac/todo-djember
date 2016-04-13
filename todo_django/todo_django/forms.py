from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):

    username = forms.CharField(max_length=30, min_length=4, label="Username")
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(), min_length=5, label="Password")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(), min_length=5, label="Confirm Password")

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError(
            "The username %s is already taken." % username)

    def clean(self):
        """
        Make sure that the two passwords match.
        """
        password = self.cleaned_data.get("password", None)
        confirm_password = self.cleaned_data.get("confirm_password", None)

        if password == confirm_password:
            return self.cleaned_data

        raise forms.ValidationError("The passwords do not match.")
