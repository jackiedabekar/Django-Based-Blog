from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
									DetailView, 
									CreateView,
									UpdateView,
									DeleteView,
									)


def home(request):
	context = {
		'posts': Post.objects.all(),
		'title' : 'Blog Post'
	}
	return render(request,'blog/home.html', context)

def about(request):
	return render(request,'blog/about.html',{'title': 'About'})

"""
The Below Portion make use of Classbased View
"""
#implementing classbased views on POST Model
#useing listbasedview to display all post in post model
class PostListView(ListView):
	model = Post
	#By default ClassedBasedViews use this format to search template ===> <app_name>/<model_name>_<viewtype>.html
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 4

#this classbeased view uses detailview
#to display particular post
class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title', 'content']

	#here we are telling and overwritting 
	#form_valid to use current login user 
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	#here we are telling and overwritting 
	#form_valid to use current login user 
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#here for user UserPassesTestMixin
	#we are checking if user login == user who created that post
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model = Post
	#this state that if post deletion is successful
	#redirect to homepage aka '/'
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

#this classbased view is created
#that when you click on username at homepage
#it will redirect to new page called as'user_post.html'
#with all the post created by that user 
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')