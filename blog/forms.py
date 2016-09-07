__author__ = 'Rom54'
from django import forms
from .models import Comment,Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'about',
            'image',
            'message',
        ]
class AddCommentForPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'message'
        ]

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user