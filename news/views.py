from django.shortcuts import render,get_object_or_404,redirect
from .models import Novosti,Comment
from django.core.paginator import Paginator
from .forms import CommentForm

"""All news"""

def news_list (request):
    contact_list = Novosti.objects.all()
    paginator = Paginator(contact_list, 2)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    if page == '1':
        return redirect('list_news', permanent=True)
    return render(request, 'news/news_list.html', {'contacts': contacts})

""" 1 new   """
def new_single (request, pk):
    new = get_object_or_404(Novosti, id=pk)
    comment = Comment.objects.filter(id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect('new_single', pk)
    else:
        form = CommentForm()
    return render(request, 'news/new_single.html', {"form": form, "comments": comment, "new": new})
