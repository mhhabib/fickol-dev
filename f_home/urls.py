from django.urls import path
from .views import PostCreateView, PostListView, UserContribution, PostUpdate, PostDelete, PostDetailView, TeachCreateView,SearchView

# from .views import MyView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('tech/', TeachCreateView.as_view(), name='tech'),
    path('new-contribute/', PostCreateView.as_view(), name='post-create'),
    path('contribution/', UserContribution.as_view(), name='contribution'),
    path('post-update/<str:pk>/', PostUpdate.as_view(), name='post-update'),
    path('post-delete/<str:pk>/', PostDelete.as_view(), name='post-delete'),
    path('d/<str:pk>/', PostDetailView.as_view(), name='details'),
    path('search/', SearchView, name='search'),

]
