from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='Twitter Username', max_length=20)
    since = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
