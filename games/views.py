from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from .models import CommentGame
from .forms import CommentGameForm
# Create your views here.


def game2048(request):
    comments = CommentGame.objects.all()[:10:]
    form = CommentGameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.get_full_path())
    return render(request,'2048.html',{'comments':comments,'form':form})

