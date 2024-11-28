from django.urls import path
from . import views

urlpatterns = [
    path('recipes/create', views.recipe_create_view, name="recipe-create"),
    path('recipes/update/<int:id>/', views.recipe_update_view, name="recipe-update"),
    path('recipes/list/', views.recipe_list_view, name="recipe-list"),
    path('recipes/detail/<int:id>/', views.recipe_detail_view, name="recipe-detail"),
]
