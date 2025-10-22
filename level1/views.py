from django.shortcuts import render, get_object_or_404
from .models import Recipe, Author
from django.db.models import Avg,Count
from django.views import View
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import CreateView

# Create your views here.

class recipesList(View):
    def get(self, request):
        # count=Recipe.aggregate(Count('Time_of_preparing'))
        # avg= Recipe.aggregate(Avg('Time_of_preparing'))
        return render(request,'recipesList.html',{'recipe':Recipe.objects.all})

class recipeDetails(DetailView):
    template_name = 'recipeDetails.html'
    model = Recipe
    context_object_name = 'onerecipe'

class  search_by_name(DetailView):
    def get(selfself,request):
        n = request.GET.get('name')
        recipe = Recipe.objects.filter(name__contains=n)
        return render(request, 'byName.html', {'recipe': recipe})

class search_by_level(DetailView):
    def get(selfself, request):
        level = request.GET.get('level')
        recipe = Recipe.objects.filter(level=level)
        return render(request, 'byLevel.html', {'recipe': recipe})

class createRecipe(CreateView):
    template_name = 'recipesForm.html'
    model = Recipe
    fields = '__all__'

class createAuthor(CreateView):
    template_name = 'authorForm.html'
    model = Author
    fields = '__all__'

# def recipeDetails(request, slug):
#     recipe = get_object_or_404(Recipe, slug=slug)
#     return render(request, 'recipeDetails.html', {"onerecipe": recipe})

# def search_by_level(request, level):
#     recipe = Recipe.objects.filter(level=level)
#     return render(request, 'byLevel.html', {'recipe': recipe})
# def search_by_name(request):
#     n=request.GET.get('name')
#     recipe = Recipe.objects.filter(name__contains=n)
#     return render(request,'byName.html',{'recipe':recipe})
