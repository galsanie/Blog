from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote
from django.http import Http404


def post_update(request, post_slug):
	if not request.user.is_staff:
		raise Http404
	item = Post.objects.get(slug=post_slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=item)
	if form.is_valid():
		form.save()
		messages.info(request, "Hey, you just changed a blog post!")
		return redirect ("posts:detail", post_slug=item.slug)

	context = {
		"form": form,
		"item": item,
	}


	return render(request, 'post_update.html', context)

def post_list(request):
	objects = Post.objects.all()#.order_by('title') <==this could be added here in case you want to ovverride the Model ordering
	paginator = Paginator(objects, 2)
	number = request.GET.get ('page')
	try:
		objects = paginator.page(number)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
	context = {
		"post_items": objects,
	}
	return render(request, "post_list.html", context)

def post_detail(request, post_slug):
	item = get_object_or_404 (Post, slug=post_slug)
	context = {
		"item": item,
	}
	return render(request, "post_detail.html", context)

def post_create(request):
	if not request.user.is_staff:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Awesome, you just added a blog post!")
		return redirect("posts:list")
	context = {
		"form": form
	}
	return render(request, "post_create.html", context)

def post_delete(request, post_slug):
	if not request.user.is_staff:
		raise Http404
	Post.objects.get(slug=post_slug).delete()
	messages.warning(request, "All cleaned up! Post deleted!")
	return redirect("posts:list")


# Create your views here.
