from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from blog.models import Blog
from blog.models import ClimbingAreas


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


class ClimbingAreaForm(forms.ModelForm):
    class Meta:
        model = ClimbingAreas
        fields = (
            'title',
            'location',
            'content',
            'number_of_routes',
        )
