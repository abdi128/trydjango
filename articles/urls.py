from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('articles/<slug:pk>/',views.articles,name="articles"),
    path('search/',views.article_search_view,name="search"),
    path('create/',views.create,name="create"),
]
