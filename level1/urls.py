
# from django.contrib import admin
from django.urls import path,include
# import level1.views as v
from .views import recipesList,recipeDetails,search_by_name,search_by_level,createRecipe,createAuthor
urlpatterns = [

    path("", recipesList.as_view(), name="recipesList"),
    path("/recipeDetails/<slug:slug>", recipeDetails.as_view(), name="recipeDetails"),
    path("byName", search_by_name.as_view(), name="byName"),
    path("byLevel/<int:level>", search_by_level.as_view(), name="byLevel"),
    path("/recipe_form", createRecipe.as_view(), name="recipesForm"),
    path("/author", createAuthor.as_view(), name="authorForm")
    # path("", v.recipesList, name="recipesList"),
    # path("" "<slug:slug>", v.recipeDetails, name="recipeDetails"),
    # path("byName", v.search_by_name, name="byName"),
    # path("byLevel/<int:level>", v.search_by_level, name= "byLevel")
]