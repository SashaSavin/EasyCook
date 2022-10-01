from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.db.models import F
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView #UpdateView, DeleteView #TODO
from cook.models import Ingredient, Recipe, UserIngredient
from django.db.models import Q
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeGenerationForm


def home_view(request):
    return render(request, "main.html", {})

# тут делаем функцию
class IngredientListObjectsView1(ListView):
    model = Ingredient
    template_name = 'action1.html'
    context_object_name = 'food'


class IngredientListObjectsView2(ListView):
    model = Ingredient
    template_name = 'action2.html'
    context_object_name = 'food'


class RecipeListObjectsView(ListView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipe'


class RecipeDetailObjectsView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe_detail'


class CustomSuccessMessageMixin:
    '''Класс для отображения сообщений'''

    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class AddCreateViewRecipe(CustomSuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'add_recipe.html'
    fields = ['title', 'ingredients', 'description', 'image']
    success_url = '/'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_msg = 'Запись создана'


class AddCreateViewIngredient(CustomSuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'add_ingredient.html'
    fields = ['title', 'image']
    success_url = '/'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_msg = 'Запись создана'


# class RecipeUpdateView(CustomSuccessMessageMixin, LoginRequiredMixin, UpdateView): #TODO
#     model = Recipe
#     template_name = 'edit_recipe.html'
#     fields = 'image', 'title', 'desc'
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'
#     success_url = '/'
#     success_msg = 'Запись обновлена'
#
#
# class RecipeDeleteView(LoginRequiredMixin, DeleteView): #TODO
#     '''Класс для удаления постов'''
#     model = Recipe
#     template_name = 'delete_recipe.html'
#     success_url = '/'
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'


class SearchResultsView(ListView):
    '''Класс для поиска'''
    model = Recipe
    template_name = 'search_results.html'
    context_object_name = 'recipe_search'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(Q(ingredients__icontains=query))
        return object_list


class ProjectLoginView(AuthUserForm, LoginView):
    form_class = AuthUserForm
    template_name = 'login.html'
    success_url = '/account'

    def get_success_url(self):
        '''Переопределение метода get_success_url на success_url'''
        return self.success_url


class RegisterUserView(CustomSuccessMessageMixin, CreateView):
    model = User
    template_name = 'register.html'
    success_url = '/login'
    form_class = RegisterUserForm
    success_msg = "Пользователь создан"


class ProjectLogoutView(LogoutView):
    '''Класс выхода'''
    next_page = '/'


def home_view(request):
    return render(request, "main.html", {})

def account_view(request):
    return render(request, "account.html", {})


def recipe_generation_view(request):
        ingrs = UserIngredient.objects.all()
        if request.method == 'POST':
            form = RecipeGenerationForm(request.POST)
            if form.is_valid():
                 ingredient = form.cleaned_data['ingredient']
                 user_ingredient = UserIngredient.objects.create(author=request.user, elem=ingredient)
                 return HttpResponseRedirect('.')
        
        else:
            form = RecipeGenerationForm()
            
        return render(request, 'recipe_gen.html', {'form': form, 'ingrs': ingrs})


def recipe_from_user_view(request):
    recipes = Recipe.objects.values('user_ingrs').values()
    return render(request, 'recipe_from_pr.html', {'recipes': recipes})
