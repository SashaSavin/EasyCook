from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView #UpdateView, DeleteView #TODO
from cook.models import Ingredient, Recipe
from django.db.models import Q
from .forms import AuthUserForm, RegisterUserForm, RecipeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


def home_view(request):
    return render(request, "main.html", {})


class IngredientListObjectsView1(ListView):
    model = Ingredient
    template_name = 'action1.html'
    context_object_name = 'food'


class IngredientListObjectsView2(ListView):
    model = Ingredient
    template_name = 'action2.html'
    context_object_name = 'food'


class RecipeDetailObjectsView(ListView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipe'

    def choice(request):
        if request.method == 'POST':
            form = RecipeForm(request.POST)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.user = request.user
                recipe.save()
        else:
            form = RecipeForm()

        return render(request, 'recipe.html', {"recipe_form": form})


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
    context_object_name = 'post'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(Q(ingredients__icontains=query) | Q(title__icontains=query))
        return object_list


class ProjectLoginView(AuthUserForm, LoginView):
    form_class = AuthUserForm
    template_name = 'login.html'
    success_url = '/'

    def get_success_url(self):
        '''Переопределение метода get_success_url на success_url'''
        return self.success_url


class RegisterUserView(CustomSuccessMessageMixin, CreateView):
    model = User
    template_name = 'register.html'
    success_url = '/'
    form_class = RegisterUserForm
    success_msg = "Пользователь создан"


class ProjectLogoutView(LogoutView):
    '''Класс выхода'''
    next_page = '/'
