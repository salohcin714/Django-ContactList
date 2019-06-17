from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField()
    address = forms.CharField(max_length=64)
    city = forms.CharField(max_length=32)
    state = forms.CharField(max_length=2)
    zip = forms.CharField(max_length=5)
    phone = forms.CharField(max_length=10)
