from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from movies.models import MoviesBlog,CommentForMoveis
from taggit.models import Tag
from movies.forms import AddMovie
from blog.models import Likes, get_count_likes, get_count_dislikes
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator,Page
import json

CONTENT_TYPE = ContentType.objects.get_for_model(MoviesBlog)
PER_PAGE = 3

def listMovies(request,page = 1):
    current_page  = Paginator(MoviesBlog.objects.all(),PER_PAGE)
    if request.POST:
        author = request.user
        movie_id = request.POST["movie_id"]
        text = request.POST["text"]
        try:
            movie = MoviesBlog.objects.get(id = movie_id)
            if text.__len__() < 1:
                raise ValueError
            CommentForMoveis.objects.create(user = author, movie_key = movie, text = text)
        except ObjectDoesNotExist:
            return HttpResponse('Обьект не найдет')
        except ValueError:
            return HttpResponse("Длина сообщения должна быть не менее 1-го символа")

    tags = Tag.objects.all()
    return render(request, 'movies.html', {'movies':current_page.page(page), 'alltags':tags} )

def listForTags(request,slug):
    return render(request,'movies.html',{'slug':slug, 'movies':MoviesBlog.objects.filter(tags__name__in = [slug])})


def like(request,inf,id):
    if not request.user.is_authenticated:
        return HttpResponse('')
    try:
        if inf == "true":
            like_generic = Likes.objects.get(content_type=CONTENT_TYPE, user_id=request.user.id, object_id=id, like=True)
            like_generic.delete()
        if inf == "false":
            like_generic = Likes.objects.get(content_type=CONTENT_TYPE,user_id=request.user.id, object_id=id, like=False)
            like_generic.delete()
    except ObjectDoesNotExist:
        like_generic,key = Likes.objects.get_or_create(content_type=CONTENT_TYPE, user_id=request.user.id, object_id=id)
        if inf == "true":
            like_generic.like = True
            like_generic.save()
        if inf == "false":
            like_generic.like = False
            like_generic.save()

    count_likes = get_count_likes(id, MoviesBlog)
    count_dislikes = get_count_dislikes(id, MoviesBlog)
    return HttpResponse(json.dumps({'dislike':count_dislikes,
                                    'like':count_likes}), content_type="application/json")


def addmovie(request):
    if request.user.is_staff or request.user.is_superuser:
        form = AddMovie(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()
            return HttpResponseRedirect('/movies/')
    return render(request,'add_movie.html',{'form_movie':form})
