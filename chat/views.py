from django.shortcuts import render,render_to_response

# Create your views here.
def front_chat(request):
    return render_to_response('chat.html',{})

