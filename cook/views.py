from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from cook.models import Ingredient, Recipe
from django.db.models import Q
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class ListObjectsView(ListView):
    model = Ingredient
    template_name = 'main.html'
    context_object_name = 'posts'


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
