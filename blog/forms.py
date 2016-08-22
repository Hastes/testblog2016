__author__ = 'Rom54'
from django import forms
from .models import Comment,Post

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