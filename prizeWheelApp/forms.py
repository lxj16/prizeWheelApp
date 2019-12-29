from django import forms
from django.core.validators import RegexValidator
my_validator = RegexValidator(
    r"(^778|^604)[0-9]{7}$", "Your phone number should be a 10 digits, starts with either 778 or 604")


class PhoneInput(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter your phone number', "id":"phoneNumber"}),
        validators=[my_validator])

    def __str__(self):
        return self.phone
