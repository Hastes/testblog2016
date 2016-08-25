from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from .models import Post, Comment, Offtop_Comment
from django.core.paginator import Paginator
from ipware.ip import get_ip
from  django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import User
from  django.core import serializers
from django.http import Http404
from blog.API.serializers import Offtop_CommentSerializer
import json
from blog.forms import CreatePostForm,AddCommentForPost
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
        form = CreatePostForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/')
    else:
        raise Http404
    return render(request,'created.html',{'form':form})

def update_article(request, article_id=None):
    instance = get_object_or_404(Post,id=article_id)
    form = CreatePostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return HttpResponseRedirect('/')
    args = {
        'instance':instance,
        'form':form,
    }
    return render(request,'created.html',args)

def delete_article(request, article_id=None):
    objects = get_object_or_404(Post, id=article_id)
    objects.delete()
    Comment.objects.filter(comment_post=article_id).delete()
    return HttpResponseRedirect('/')

def front(request,page_number=1):
    comment_count = Comment.objects.count()
    objects = Post.objects.all()
    search = request.GET.get('q')
    if search:
        objects = Post.objects.filter(title__icontains=search)
    current_page = Paginator(objects,count_page)
    return render(request,'posts.html',{'objects':current_page.page(page_number),'comment_count':comment_count,'get_ip':get_ip(request)})

def userprofile(request,username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404
    return render(request,'userprofile.html',{'user':user})

def likepost(request, article_id):
    like = Post.objects.get(id=article_id)
    like.likes_post +=1
    like.save()
    return HttpResponse('')

def message_like(request, message_id):
    like = Offtop_Comment.objects.get(id=message_id)
    like.likes+=1
    like.save()
    return HttpResponse()

def register_user(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        user_form = UserCreationForm(request.POST)
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
    objects= Offtop_Comment.objects.all()
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

def testpage(request):
    return render(request,'index.html',{})
def testpage2(request):
    return  render(request,'test.html',{})