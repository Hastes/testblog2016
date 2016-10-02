from django import forms
from django.contrib.auth.models import User
from movies.models import CommentForMoveis,MoviesBlog
class AddCommentForMovie(forms.ModelForm):
    class Meta:
        model = CommentForMoveis
        fields = [
            'text'
        ]

class AddMovie(forms.ModelForm):
    class Meta:
        model = MoviesBlog
        fields = [
            'youtube_key',
            'tags'
        ]