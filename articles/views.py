from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from articles.forms import ArticleForm


def home(request):

    article_all = Article.objects.all()
#    my_list = [23, 234, 325, 3526, 666, 77, 232]
    context = { 'article_all':article_all, "user": request.user }

    ttemplates = render_to_string("home.html", context=context)
#   HTML_TEST= "<h1>Title: {title}</h1><h2>ID: {id}</h2><h3>Content: {content}</h3>".format(**context)
    return render(request, "home.html", context)


def articles(request, pk):
    article = None

    if pk is not None:
        article = Article.objects.get(id=pk)
        context = { 'article':article }

    return render(request, 'articles/article.html', context)



def article_search_view(request):
    query = request.GET.get('q')

    if query is not None:
        try:
            article = Article.objects.get(id=int(query))
            return render(request, 'articles/search.html', { 'article':article })
        
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