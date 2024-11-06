from django import forms
from django.contrib.auth.models import User

from .models import ingredientDb

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'rounded-lg w-full',
            'style': 'color: black;',
        }), label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'rounded-lg w-full',
            'style': 'color: black;',
        }), label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'rounded-lg w-full',
                'style': 'color: black;'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        # Check if passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class IngredientForm(forms.ModelForm):
    ingredientName = forms.CharField(label="Ingredient")

    class Meta:
        model = ingredientDb
        fields = ['ingredientName']
