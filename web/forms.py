from django import forms
from django.contrib.auth import get_user_model

from web.models import Post

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password_repeat = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password_repeat']:
            self.add_error("password", "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ("email", "username", "password", "password_repeat")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class PostForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = Post
        fields = ('art_type', 'hours_spent', 'used_material', 'description', 'artwork', "tags")
