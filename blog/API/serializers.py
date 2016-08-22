from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ModelField,
    HyperlinkedIdentityField)

from blog.models import Offtop_Comment
from django.contrib.auth.models import User

class Offtop_CommentSerializer(ModelSerializer):
    author = SerializerMethodField()
    class Meta:
        model = Offtop_Comment
        fields = [
            'id',
            'author',
            'message',
            'likes',
            'created_date',
        ]
    def get_author(self,obj):
        return str(obj.author.username)