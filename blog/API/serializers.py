from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ModelField,
    HyperlinkedIdentityField)

from blog.models import Offtop_Comment, UserProf, English
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

    def get_author(self, obj):
        return str(obj.author.username)


class UserProfSerializer(ModelSerializer):
    user_key = SerializerMethodField()

    class Meta:
        model = UserProf
        fields = [
            'user_key_id',
            'user_key',
            'rank_name',
            'get_count_lk',
            'reputation',
            'avatar',
        ]

    def get_user_key(self, obj):
        return str(obj.user_key.username)


class EngilshSerializer(ModelSerializer):
    class Meta:
        model = English
        fields = [
            'lesson_number',
            'vocabulary',
            'story',
            'cultural_notes',
            'action',
        ]
