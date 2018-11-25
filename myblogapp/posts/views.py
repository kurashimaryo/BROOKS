from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post

def index (request):
 #   return HttpResponse("HelloWorld")
     posts = post.objects.order_by('-published')
     return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request,post_id):
    post1 = get_object_or_404(post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post2': post1})

#def a(request):
#    return render(request, 'posts/1.html')
# Create your views here.
