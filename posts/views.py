from django.shortcuts import render, get_object_or_404
from .models import Post

def post_create(request):
	return render(request, 'post_create.html', {})

def post_list(request):
	objects = Post.objects.all()
	context = {
		"post_items": objects,
	}
	return render(request, 'post_list.html', context)

def post_detail(request, post_id):
	item = get_object_or_404 (Post, id=post_id)
	context = {
		"item": item, 
	}
	return render(request, "post_detail.html", context)



# Create your views here.
