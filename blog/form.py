from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from blog.models import Blog


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'last_login',
            'date_joined',
        )


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'author',
            'content',
        )
