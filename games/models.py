from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.



class CommentGame(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    comment = models.TextField(max_length=500,verbose_name="Ваш комментарий:")
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.comment

    def __str__(self):
        return self.comment
    class Meta:
        ordering = ['-date']


class Score2048(models.Model):
    user = models.OneToOneField(User)
    score_user = models.IntegerField(default=0)
    class Meta:
        ordering = ['-score_user']


