from django.shortcuts import render,get_object_or_404
from .models import Novosti


# Create your views here.
"""All news"""
def news_list (request):
    news = Novosti.objects.all()
    return render(request,'news/news_list.html',{"news": news})



"""check 1 new"""
def new_single (request, pk):
    new = get_object_or_404(Novosti, id=pk)
    return render(request, 'news/new_single.html',{"new": new})
