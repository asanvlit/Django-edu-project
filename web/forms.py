from django import forms
from django.contrib.auth import get_user_model

from web.models import Post, PostTag

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


class PostTagForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = PostTag
        fields = ('title',)


class PostFilterForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Поиск"}), required=False)
    hours_spent = forms.NullBooleanField(
        label='Потрачено времени',
        widget=forms.Select(
            choices=(
                ('unknown', 'Неизвестно'),
                ('true', 'В течение дня'),
                ('false', 'Больше одного дня')
            )
        )
    )
    published_at_after = forms.DateTimeField(
        label='От',
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}, format='%Y-%m-%dT%H:%M'
        ),
        required=False
    )
    published_at_before = forms.DateTimeField(
        label='До',
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}, format='%Y-%m-%dT%H:%M'
        ),
        required=False
    )
