from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

def upload_url(post, nameimage):
    return '%s\%s\%s' % (post.author, post.title, nameimage)
def get_count_likes(id,model):
    return Likes.objects.filter(content_type=ContentType.objects.get_for_model(Post),object_id=id).count()
def get_count_comment(id):
    return Comment.objects.filter(comment_post=id).count()


# class UserProfile(User):
#     image = models.ImageField(null=True,
#                           blank=True,
#                           upload_to=upload_url,
#                           verbose_name='Аватарка',
#                           width_field="width_field",
#                           height_field="heigth_field")
#     width_field = models.IntegerField(null=True,default=0)
#     heigth_field = models.IntegerField(null=True,default=0)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    about = models.CharField(max_length=40, verbose_name='Описание')
    message = models.TextField(verbose_name='Текст')
    likes_post = models.IntegerField(default=0)
    image = models.ImageField(null=True,
                              blank=True,
                              upload_to=upload_url,
                              verbose_name='Постер',
                              width_field="width_field",
                              height_field="heigth_field"
                              )
    width_field = models.IntegerField(null=True,default=0)
    heigth_field = models.IntegerField(null=True,default=0)
    created_date = models.DateTimeField(default=timezone.now)
    def get_count_lk(self):
        return get_count_likes(self.id,Post)
    def get_count_com(self):
        return get_count_comment(self.id)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={'article_id': self.id})
        # return '/article/%s/' % (self.id)

    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    message = models.TextField(max_length=300)
    comment_post = models.ForeignKey(Post)
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

class Offtop_Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    message = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    def get_count_lk(self):
        return get_count_likes(self.id,Offtop_Comment)
    def __unicode__(self):
        return '%s %s' % (self.author, self.message)

    def __str__(self):
        return 'Author: %s Text: %s' % (self.author, self.message)

    class Meta:
        ordering = ['-created_date']

class Likes(models.Model):
    like = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    user_id = models.PositiveIntegerField()
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class UserProf(models.Model):
    user_key = models.OneToOneField(User)
    rank = models.IntegerField(default=0)
    rank_name = models.CharField(max_length=10,default='НОУНЕЙМ')
    def get_count_lk(self):
        return get_count_likes(self.id,UserProf)
