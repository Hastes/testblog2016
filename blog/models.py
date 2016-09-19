from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from pyuploadcare.dj.models import ImageField
#from annoying.fields import AutoOneToOneField

def upload_url(post, nameimage):
    return '%s\%s\%s' % (post.author, post.title, nameimage)
def upload_url_for_user(user,nameimage):
    return 'userprofile\%s\%s' % (user.user_key.username,nameimage)
def get_count_likes(id,model):
    return Likes.objects.filter(content_type=ContentType.objects.get_for_model(model),object_id=id).count()
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
    # image = models.ImageField(null=True,
    #                           blank=True,
    #                           upload_to=upload_url,
    #                           verbose_name='Постер',
    #                           width_field="width_field",
    #                           height_field="heigth_field",
    #                           )
    # width_field = models.IntegerField(null=True,default=0)
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
    message = models.TextField(max_length=300)
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
    def get_count_lk(self):
        return get_count_likes(self.user_key_id,UserProf)

    # def validate_image(fieldfile_obj):
    #     filesize = fieldfile_obj.file.size
    #     limit = 300.0
    #     if filesize > limit*1024:
    #         raise ValidationError("Максимальный размер изображения %sKB" % str(limit))

    avatar = ImageField(verbose_name="Аватар",null=True,manual_crop="")
    # width_field = models.IntegerField(null=True,default=0)
    # heigth_field = models.IntegerField(null=True,default=0)
    user_key = models.OneToOneField(User,primary_key=True,related_name="user_prof")
    rank_name = models.CharField(max_length=10,default='НОУНЕЙМ')
    reputation = models.IntegerField(default=0)
    #score2048 = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return str(self.user_key.username)
    def __str__(self):
        return str(self.user_key.username)
    class Meta:
        ordering = ['-reputation']

class NewsProfile(models.Model):
    key = models.ForeignKey(UserProf)
    news = models.TextField(max_length=120,verbose_name="Что у вас нового?")
    date = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-date']

class English(models.Model):
    lesson_number = models.IntegerField(unique=True)
    vocabulary = models.TextField()
    story = models.TextField()
    cultural_notes = models.TextField()
    action = models.TextField()
    communicaton_skills = models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.lesson_number)
    class Meta:
        ordering= ['lesson_number']

class ImagePostPicture(models.Model):
    key = models.OneToOneField(Post,related_name="img_post")
    image = ImageField(verbose_name="Постер(не обязательно)",blank=True,manual_crop="")
    text = models.TextField()



#User._meta.get_field('username').max_length = 11
#User._meta.get_field('username').help_text = 'Обязательное поле. Не более 11 символов. Только буквы, цифры и символы @/./+/-/_.'

