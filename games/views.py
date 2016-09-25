from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse

from .models import CommentGame, Score2048
from .forms import CommentGameForm
# Create your views here.


def game2048(request):
    comments = CommentGame.objects.all()[:10:]
    recordmans = Score2048.objects.all()[:10:]
    form = CommentGameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.get_full_path())
    return render(request,'2048.html',{'comments':comments,'form':form,'recordmans':recordmans})

def score(request):
    if request.user.is_authenticated:
        obj,key = Score2048.objects.get_or_create(user=request.user)
        score = int(request.POST.get('score',False))
        if obj.score_user < score:
            obj.score_user = score
            obj.save()
            return HttpResponse('Ваш новый рекорд %s' % score)
    return HttpResponse()

def save_canvas(request):
    if request.POST:
        clickX = request.POST.get('clickX',False)
        clickY = request.POST.get('clickY',False)
        clickDrag = request.POST.get('clickDrag',False)
    return HttpResponse()

def painters(request):
    return render_to_response('painters.html',{})

