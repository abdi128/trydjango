from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
import random



def home(request):
    number = random.randint(1, 4)

    article_obj1 = Article.objects.create(title="titleOne",content="contentOne")
    article_obj2 = Article.objects.create(title="titleTwo",content="contentTwo")
    article_obj3 = Article.objects.create(title="titleThree",content="contentThree")
    article_obj4 = Article.objects.create(title="titleFour",content="contentFour")

    article_test = Article.objects.get(id=number)
    my_list = [23, 234, 325, 3526, 666, 77, 232]
    context = {
        'title' : article_test.title,
        'id' : article_test.id,
        'content' : article_test.content,
        'my_list' : my_list,
    }

    ttemplates = render_to_string("home.html", context=context)

#   HTML_TEST= "<h1>Title: {title}</h1><h2>ID: {id}</h2><h3>Content: {content}</h3>".format(**context)
    
    return HttpResponse(ttemplates)