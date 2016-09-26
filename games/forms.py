__author__ = 'Rom54'
from django import forms
from .models import CommentGame

class CommentGameForm(forms.ModelForm):
    class Meta:
        model = CommentGame
        fields = [
            'comment',
        ]
