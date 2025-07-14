from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'blog/index.html',{})

def post(request,slug):
    post = get_object_or_404(Post,slug=slug) 
    if request.method == 'GET':
         return render(request,'blog/post.html',{'post': post})
    elif request.method == 'POST':
         body = request.POST.get('body')
         comment = Comment(body=body,author=UserProfile.objects.last(),post=Post.objects.get(slug=slug))
         comment.save()
         return render(request,'blog/post.html',{'post': post})
     
@login_required  
def posts(request): 
    if request.method == 'POST':
        body = request.POST['body']
        title = request.POST['body'][:10]
        post=Post(body=body,title=title,author=request.user.userprofile)
        post.save()
        all_posts = Post.objects.all().order_by('-created_at')
        return render(request,'blog/posts.html',{'all_posts': all_posts})
    elif request.method == 'GET':
        all_posts = Post.objects.all().order_by('-created_at')
        return render(request,'blog/posts.html',{'all_posts': all_posts})