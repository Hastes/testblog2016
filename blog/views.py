from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from .models import Post, Comment, Offtop_Comment, Likes, UserProf,English,NewsProfile,ImagePostPicture
from django.core.paginator import Paginator
from ipware.ip import get_ip
from  django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from  django.core import serializers
from django.contrib import sessions
from django.http import Http404
from django.utils.text import slugify
from blog.API.serializers import Offtop_CommentSerializer, UserProfSerializer,EngilshSerializer
import json
from blog.forms import CreatePostForm,AddCommentForPost,AddNewsProfile,ImagePostPictureForm,UserSettingsForm
from django.http import JsonResponse
# Create your views here.
count_page=2

def get_ip_user(request):
    return HttpResponse(json.dumps({'get_ip':get_ip(request)}), content_type="application/json")

def article(request, article_id=None):
    objects = get_object_or_404(Post, id=article_id)
    form = AddCommentForPost(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.comment_post = objects
        instance.save()
        return HttpResponseRedirect(objects.get_absolute_url())
    return render(request,'single.html',{'objects':objects,'comments':Comment.objects.filter(comment_post=article_id),'form':form})

def created_post(request):
    if request.user.is_staff or request.user.is_superuser:
        form = CreatePostForm(request.POST or None)
        formimg = ImagePostPictureForm(request.POST or None)
        if form.is_valid() & formimg.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            instance_img = formimg.save(commit=False)
            instance_img.key = instance
            instance_img.save()
            return HttpResponseRedirect('/')
    else:
        raise Http404
    return render(request,'created.html',{'form':form,'formimg':formimg})

def update_article(request, article_id=None):
    instance = get_object_or_404(Post,id=article_id)
    instance_img = ImagePostPicture.objects.get(key = instance)
    form = CreatePostForm(request.POST or None,request.FILES or None,instance=instance)
    formimg = ImagePostPictureForm(request.POST or None,instance= instance_img )
    if form.is_valid() & formimg.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        instance_img = formimg.save(commit=False)
        instance_img.key = instance
        instance_img.save()
        return HttpResponseRedirect('/')
    args = {
        'form':form,
        'formimg':formimg,
    }
    return render(request,'created.html',args)

def delete_article(request, article_id=None):
    if request.user.is_superuser:
        objects = get_object_or_404(Post, id=article_id)
        objects.delete()
        Comment.objects.filter(comment_post=article_id).delete()
    return HttpResponseRedirect('/')

def front(request,page_number=1):
    objects = Post.objects.all()
    search = request.GET.get('q')
    if search:
        objects = Post.objects.filter(title__icontains=search)
    current_page = Paginator(objects,count_page)
    return render(request,'posts.html',{'objects':current_page.page(page_number)})

def userprofile(request,username):
    user = get_object_or_404(User,username=username)
    get_news = NewsProfile.objects.filter(key = user.id)[:15:]
    content_type = ContentType.objects.get_for_model(UserProf)
    try:
        UserProf.objects.get(user_key=user)
    except ObjectDoesNotExist:
        UserProf.objects.update_or_create(user_key=user)
    user_inf = UserProf.objects.get(user_key=user)
    rank = Likes.objects.filter(content_type=content_type,object_id=user_inf.user_key_id).count()
    user_inf.rank = rank
    user_inf.save()
    form_news = None
    if user.username == request.user.username:
        form_news = AddNewsProfile(request.POST or None)
        formimg = UserSettingsForm(request.POST or None,instance=user_inf)
        if form_news.is_valid() & formimg.is_valid():
            form = form_news.save(commit=False)
            form.key = user_inf
            form.save()
            formimg = formimg.save(commit=False)
            formimg.user_key = user
            formimg.save()
            return HttpResponseRedirect(request.get_full_path())
    else:
        form_news = None
        formimg = None
    if not request.user.is_authenticated:
        return render(request,'userprofile.html',{'user':user,'user_inf':user_inf,'get_news':get_news})
    try:
        Likes.objects.get(content_type=content_type,user_id=request.user.id,object_id=user_inf.user_key_id)
        visible_btn = False
        print(visible_btn)
    except ObjectDoesNotExist:
        visible_btn = True
    return render(request,'userprofile.html',{'user':user,'user_inf':user_inf,'visible':visible_btn,'news':NewsProfile.objects.all(),
                                              'formimg':formimg,'form_news':form_news,'get_news':get_news})

def add_rep_user(request,id_user):
    if not request.user.is_authenticated:
        return HttpResponse('')
    if id_user == str(request.user.id):
        return HttpResponse('ЧСВ')
    content_type = ContentType.objects.get_for_model(UserProf)
    try:
        like_generic = Likes.objects.get(content_type=content_type,user_id=auth.get_user(request).id,object_id=id_user)
        like_generic.delete()
    except ObjectDoesNotExist:
        like_generic = Likes.objects.create(content_type=content_type,
                                            user_id=request.user.id,
                                            object_id=id_user,
                                            like=True
                                            )
    return HttpResponse(Likes.objects.filter(content_type=content_type,object_id=id_user).count())

# def likepost(request, article_id):
#     if not request.session.get('has_liked'+article_id, False):
#         like_generic = Likes.objects.create(content_type=ContentType.objects.get_for_model(Post),user_id=request.user.id,object_id=article_id)
#     if request.session.get('has_liked'+article_id, False):    #1 false  #2... true
#         like_generic.count_likes -=1
#         like_generic.save()
#         del request.session['has_liked'+article_id]
#     else:
#         like_generic.count_likes +=1
#         like_generic.save()
#         request.session['has_liked'+article_id] = True
#     return HttpResponse(like_generic.count_likes)

def likepost(request, article_id):
    if not request.user.is_authenticated:
        return HttpResponse('')
    content_type = ContentType.objects.get_for_model(Post)
    try:
        like_generic = Likes.objects.get(content_type=content_type,user_id=request.user.id,object_id=article_id)
        like_generic.delete()
    except ObjectDoesNotExist:
        print('is None')
        like_generic = Likes.objects.create(content_type=content_type,
                                            user_id=request.user.id,
                                            object_id=article_id,
                                            like=True
                                            )
    return HttpResponse(Likes.objects.filter(content_type=content_type,object_id=article_id).count())

def message_like(request, message_id):
    like = Offtop_Comment.objects.get(id=message_id)
    like.likes+=1
    like.save()
    return HttpResponse()

def register_user(request):
    args = {}
    args['form'] = UserCreateForm()
    if request.POST:
        user_form = UserCreateForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            login(request, authenticate(username=request.POST['username'], password=request.POST['password1']))
            return HttpResponseRedirect('/')
        else:
            args['form']= user_form
    return render(request,'register.html',args)

def login_user(request):
    args = {}
    args['form']= AuthenticationForm()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            err = "User not found 404 or incorrect password"
            return render(request,'login.html',{'errorlog':err,'form':args['form']})
    return render(request,'login.html',args)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def offtop(request):
    # objects= Offtop_Comment.objects.all()
    return render(request,'offtop.html',{})

def offtopjs(request):
    if request.method == 'POST':
        message = request.POST["messs"]
        if message!= "":
            Offtop_Comment.objects.create(author=request.user,message=message)
    return HttpResponse()

def offtop_reload(request):
    args = {}
    obj  = Offtop_Comment.objects.all()
    args['objects']= Offtop_CommentSerializer(obj,many=True).data
    return HttpResponse(json.dumps(args), content_type="application/json")

def delete_message(request):
    user = get_user(request)
    if user.is_superuser:
        Offtop_Comment.objects.all().delete()
    else:
        raise Http404
    return HttpResponse()

def users_section(request):
    args = {}
    userprof = UserProf.objects.all()[:5:]
    try:
        UserProf.objects.get(user_key=request.user)
        req_user = UserProf.objects.filter(user_key=request.user)
        args['request_user'] = UserProfSerializer(req_user,many=True).data
    except:
        pass
    args['user_section'] = UserProfSerializer(userprof,many=True).data
    return HttpResponse(json.dumps(args), content_type="application/json")

def english_get(request,pk):
    obj = English.objects.get(id=pk)
    args = {}
    args['eng']= EngilshSerializer(obj).data
    return HttpResponse(json.dumps(args),content_type="application/json")


def english_met(request):
    return render(request,'english.html',{'eng':English.objects.all()})
def testpage(request):
    return render(request,'index.html',{})
def testpage2(request):
    return render(request,'pusher.html',{})