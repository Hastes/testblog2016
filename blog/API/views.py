from rest_framework.generics import ListAPIView
from blog.models import Offtop_Comment, UserProf
from .serializers import Offtop_CommentSerializer, UserProfSerializer


class Offtop_CommentAPIView(ListAPIView):
    queryset = Offtop_Comment.objects.all()
    serializer_class = Offtop_CommentSerializer


class UserProfAPIView(ListAPIView):
    queryset = UserProf.objects.all()
    serializer_class = UserProfSerializer
