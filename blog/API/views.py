from rest_framework.generics import ListAPIView
from blog.models import Offtop_Comment
from .serializers import Offtop_CommentSerializer

class Offtop_CommentAPIView(ListAPIView):
    queryset = Offtop_Comment.objects.all()
    serializer_class = Offtop_CommentSerializer