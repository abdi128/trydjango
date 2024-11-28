from django.http import HttpResponse, Http404
from articles.models import Article
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from articles.forms import ArticleForm
from django.db.models import Q


def home(request):

    article_all = Article.objects.all()
#    my_list = [23, 234, 325, 3526, 666, 77, 232]
    context = { 'article_all':article_all, "user": request.user }

    ttemplates = render_to_string("home.html", context=context)
#   HTML_TEST= "<h1>Title: {title}</h1><h2>ID: {id}</h2><h3>Content: {content}</h3>".format(**context)
    return render(request, "home.html", context)


def articles(request, pk=None):
    article = None
    if pk is not None:
        try:
            article = Article.objects.get(slug=pk)
        except:
            """messages.error(request, f"This url: \"http://127.0.0.1:8000/articles/{pk}\"  doesn\'t exist")
            return redirect('home')"""
            raise Http404
    context = { 'article':article }
    return render(request, 'articles/article.html', context)



def article_search_view(request):
    query = request.GET.get('q')

    qs = Article.objects.all()
    result = 0

    if query is not None:
        try:
            #lookups = Q(title__icontains=query) #| Q(content__icontains=query) 
            #qs = Article.objects.filter(lookups)
            qs = Article.objects.search(query)
            result = qs.count()
            return render(request, 'articles/search.html', { 'articles':qs, 'result':result })
        
        except(ValueError, Article.DoesNotExist):
            return redirect('home')
        
    else:
        return redirect('home')


@login_required
def create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        new_article = form.save()
        """title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        new_article = Article.objects.create(title=title, content=content)"""
        return redirect('home')
    
    return render(request, 'articles/create.html', { 'form': form })