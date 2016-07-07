from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=20)