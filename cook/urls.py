from django.urls import path
from cook.views import home_view, IngredientListObjectsView1, IngredientListObjectsView2, ProjectLoginView, \
    RegisterUserView, ProjectLogoutView, SearchResultsView, AddCreateViewIngredient, AddCreateViewRecipe, \
    RecipeDetailObjectsView
    # NeedUpdateView, PostDeleteView, #TODO

urlpatterns = [
    path('', home_view),
    path('action1/', IngredientListObjectsView1.as_view()),
    path('action2/', IngredientListObjectsView2.as_view()),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('add_recipe/', AddCreateViewRecipe.as_view(), name='add_recipe'),
    path('add_ingredient/', AddCreateViewIngredient.as_view(), name='add_ingredient'),
    path('detail/<int:pk>', RecipeDetailObjectsView.as_view(), name='recipe_detail'),
    path('login/', ProjectLoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', ProjectLogoutView.as_view(), name='logout'),
    # path('edit/<int:pk>', NeedUpdateView.as_view(), name = 'edit'), #TODO
    # path('delete/<int:pk>', PostDeleteView.as_view(), name = 'delete'), #TODO
]
