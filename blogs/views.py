from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from . forms import BlogPostForm

def index(request):
	return render(request, 'blogs/index.html')

@login_required
def get_posts(request):
	added_posts = BlogPost.objects.filter(owner=request.user).order_by('date_added')
	context = {'added_posts': added_posts}
	return render(request, 'blogs/posts.html', context)

@login_required
def add_post(request):
	if request.method != "POST":
		form = BlogPostForm()
	else:
		form = BlogPostForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.owner = request.user
			new_post.save()
			return HttpResponseRedirect(reverse('blogs:posts'))
	context = {'form': form}
	return render(request, 'blogs/add_post.html', context)

@login_required
def edit_post(request, post_id):
	original_post = BlogPost.objects.get(id=post_id)
	if request.user != original_post.owner:
		raise Http404
	if request.method == 'POST':
		form = BlogPostForm(instance=original_post, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:posts'))
	else:
		form = BlogPostForm(instance=original_post)
	context = {'original_post': original_post, 'form': form}
	return render(request, 'blogs/edit_post.html', context)

