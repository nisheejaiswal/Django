from django import forms

class RegistrationForm(forms.Form):
    firstname=forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    email=forms.EmailField()