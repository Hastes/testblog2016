from django.shortcuts import render

# Create your views here.

def trashList(request):
    return render(request,'movies.html',{})