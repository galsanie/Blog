from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_update(request, post_id):
	item = Post.objects.get(id=post_id)
	form = PostForm(request.POST or None, request.FILES or None, instance=item)
	if form.is_valid():
		form.save()
		messages.info(request, "Hey, you just changed a blog post!")
		return redirect ("posts:update", post_id=item.id)

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

def post_detail(request, post_id):
	item = get_object_or_404 (Post, id=post_id)
	context = {
		"item": item, 
	}
	return render(request, "post_detail.html", context)

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Awesome, you just added a blog post!")
		return redirect("posts:list")
	context = {
		"form": form
	}
	return render(request, "post_create.html", context)

def post_delete(request, post_id):
	Post.objects.get(id=post_id).delete()
	messages.warning(request, "Are you sure you want to delete this post?")
	return redirect("posts:list")


# Create your views here.
