from django import forms


class AdminLoginForm(forms.Form):
    username = forms.CharField(required=True,
                               max_length=100,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control'
                                   }
                               ))

    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                   }
                               ))
