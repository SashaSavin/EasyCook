from django.urls import path
from cook.views import ListObjectsView, ProjectLoginView, RegisterUserView, ProjectLogoutView, SearchResultsView
# DetailObjectsView, SearchResultsView, NeedUpdateView, PostDeleteView, PostCreateView,

urlpatterns = [
    path('', ListObjectsView.as_view()),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    # path('edit/<int:pk>', NeedUpdateView.as_view(), name = 'edit'),
    # path('delete/<int:pk>', PostDeleteView.as_view(), name = 'delete'),
    # path('create/', PostCreateView.as_view(), name = 'create'),
    # path('detail/<int:pk>', DetailObjectsView.as_view(), name='detail'),
    path('login/', ProjectLoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', ProjectLogoutView.as_view(), name='logout'),
]
