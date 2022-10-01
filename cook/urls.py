from django.urls import path
from cook.views import home_view, IngredientListObjectsView1, IngredientListObjectsView2, ProjectLoginView, \
    RegisterUserView, ProjectLogoutView, SearchResultsView, AddCreateViewIngredient, AddCreateViewRecipe, \
    RecipeListObjectsView, RecipeDetailObjectsView, account_view, recipe_generation_view, recipe_from_user_view #choice_view

# NeedUpdateView, PostDeleteView, # TODO

urlpatterns = [
    path('', home_view),
    path('action1/', IngredientListObjectsView1.as_view()),
    path('action2/', IngredientListObjectsView2.as_view()),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('add_recipe/', AddCreateViewRecipe.as_view(), name='add_recipe'),
    path('add_ingredient/', AddCreateViewIngredient.as_view(), name='add_ingredient'),
    path('recipe/', RecipeListObjectsView.as_view(), name='recipe'),
    path('<int:pk>', RecipeDetailObjectsView.as_view(), name='recipe_detail'),
    path('login/', ProjectLoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', ProjectLogoutView.as_view(), name='logout'),


    path('account/', account_view, name='account'),
    path('account/recipe_generation/', recipe_generation_view, name='recipe_generation'),
    path('account/recipe_from_user/', recipe_from_user_view, name='recipe_from_user'),
    # path('edit/<int:pk>', NeedUpdateView.as_view(), name = 'edit'), #TODO
    # path('delete/<int:pk>', PostDeleteView.as_view(), name = 'delete'), #TODO
]
