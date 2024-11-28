from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm, RecipeIngredientForm
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/list.html', { "object_list": qs })

@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    return render(request, 'recipes/detail.html', { "object": obj })

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        try:
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "You have successfully added a recipe")
            return redirect(obj.get_absolute_url())
        except:
            messages.error(request, "Something went wrong. Try Again!")
            return render(request, "recipes/create.html", {"form":form})
    
    return render(request, "recipes/create.html", {"form":form})


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    obj_2 = get_object_or_404(RecipeIngredient, recipe=obj)
    form = RecipeForm(request.POST or None, instance=obj)
    form_2 = RecipeIngredientForm(request.POST or None, instance=obj_2)
    if (form.is_valid() and form_2.is_valid()):
        try:
            form.save()
            form_2.save()
            messages.success(request, "You have successfully updated the recipe")
            return render(request, "recipes/update.html", {"form":form, "form_2":form_2, "object":obj})
        
        except:
            messages.error(request, "Something went wrong. Try Again!")
            return render(request, "recipes/update.html", {"form":form, "form_2":form_2, "object":obj})
    
    return render(request, 'recipes/update.html', {"form":form, "form_2":form_2, "object":obj})


    # nati X@mpl3!Pa$$w0rd