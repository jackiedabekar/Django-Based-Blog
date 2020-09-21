from django.urls import path
from . import views
#implementing class based view
from .views import (PostListView, 
					PostDetailView,
					PostCreateView,
					PostUpdateView,
					PostDeleteView,
                    UserPostListView)


urlpatterns = [
    #path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
    #deatilview example stick to convention
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    #this path uses classbased view to create new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete')
]	