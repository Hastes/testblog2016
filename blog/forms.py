__author__ = 'Rom54'
from django import forms
from .models import Comment,Post,NewsProfile,ImagePostPicture,UserProf
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pyuploadcare.dj.models import ImageField
from pyuploadcare.dj.forms import FileWidget


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'about',
            'message',
        ]


class AddCommentForPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'message'
        ]
class AddNewsProfile(forms.ModelForm):
    class Meta:
        model=NewsProfile
        fields = [
            'news'
        ]

class ImagePostPictureForm(forms.ModelForm):
    class Meta:
        model = ImagePostPicture
        fields = ["image"]

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProf
        fields = ["avatar"]


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