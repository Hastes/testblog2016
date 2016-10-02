from django.db import models
from django.db.utils import settings
from django.utils import timezone
from taggit.managers import TaggableManager
from blog.models import get_count_likes, get_count_dislikes

# Create your models here.
def get_count_comments(id):
    return CommentForMoveis.objects.filter(movie_key= id).count()


class MoviesBlog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    youtube_key = models.CharField(max_length=300, verbose_name="Ключ видео(последние 11 цифр ссылке на ролик)",help_text="Возможно вы ввели неправильный ключ")
    date = models.DateTimeField(default=timezone.now)
    tags = TaggableManager(blank=False)

    def get_count_lk(self):
        return get_count_likes(self.id, MoviesBlog)

    def get_count_dislikes(self):
        return get_count_dislikes(self.id, MoviesBlog)

    def get_count_comments(self):
        return get_count_comments(self.id)
    class Meta:
        ordering = ['-date']

class CommentForMoveis(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    movie_key = models.ForeignKey(MoviesBlog,related_name="comments_movies")
    text = models.TextField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']