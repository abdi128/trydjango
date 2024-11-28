from django.contrib import admin
from .models import Recipe, RecipeIngredient
from django.contrib.auth import get_user_model

User = get_user_model()
"""admin.site.unregister(User)

class UserInline(admin.StackedInline):
    model = User"""
    
class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    #fields = ['name', 'quantity', 'unit', 'directions']
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = [ 'timestamp', 'updated']
    raw_id_fields = [ 'user' ]

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'recipe']
    readonly_fields = ['timestamp', 'updated', 'quantity_as_float', 'as_mks', 'as_imperial']
    raw_id_fields = ['recipe']


"""class RecipeInline(admin.StackedInline):
    model = Recipe
    #fields = ['name', 'quantity', 'unit', 'directions']
    extra = 0

class UserAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]
    list_display = ['username']"""




admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
#admin.site.register(User, UserAdmin)